"""
Advent of Code 2015 - Day 22
https://adventofcode.com/2015/day/22
"""

import copy
import dataclasses
import heapq
import pathlib

from typing import Dict, List, Tuple

__mypath = pathlib.Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


@dataclasses.dataclass
class Spell:
    cost: int
    immediate: callable
    effect: callable
    duration: int = 0


class GameState:
    def __init__(self, player_hp: int, player_mana: int, boss_hp: int, boss_dmg: int):
        self.player_armor = 0
        self.player_hp = player_hp
        self.player_mana = player_mana
        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg
        self.spells: Dict[str, Spell] = {
            'Magic Missile': Spell(53, self._magic_missile, None),
            'Drain': Spell(73, self._drain, None),
            'Shield': Spell(113, self._shield, self._shield, 6),
            'Poison': Spell(173, None, self._poison, 6),
            'Recharge': Spell(229, None, self._recharge, 5),
        }
        self.timers: Dict[str, int] = {}
        self.mana_spent = 0
        self.spells_cast: List[str] = []

    def copy(self):
        return copy.deepcopy(self)

    @property
    def h(self):
        return self.mana_spent + self.boss_hp

    def __lt__(self, other):
        return self.h < other.h

    def available_spells(self):
        available = []
        for spell in self.spells:
            if (self.spells[spell].cost <= self.player_mana and (
                    not self.spells[spell].effect or not self.timers.get(spell, 0))):
                available.append(spell)
        return available

    def cast(self, spell: str):
        self.player_mana -= self.spells[spell].cost
        self.mana_spent += self.spells[spell].cost
        self.spells_cast += [spell]
        if self.spells[spell].immediate:
            self.spells[spell].immediate()
        if self.spells[spell].effect:
            self.timers[spell] = self.spells[spell].duration

    def process_effects(self):
        for spell in [_ for _ in self.timers if self.timers[_]]:
            self.spells[spell].effect()
            self.timers[spell] -= 1

    def boss_attack(self):
        self.player_hp -= max(1, self.boss_dmg - self.player_armor)

    def _magic_missile(self):
        self.boss_hp -= 4

    def _drain(self):
        self.boss_hp -= 2
        self.player_hp += 2

    def _shield(self):
        if not self.timers.get('Shield', False):
            self.player_armor += 7
        elif self.timers['Shield'] == 1:
            self.player_armor -= 7

    def _poison(self):
        self.boss_hp -= 3

    def _recharge(self):
        self.player_mana += 101


def optimal_spells(player_hp: int = 50, player_mana: int = 500,
                   boss_hp: int = 51, boss_dmg: int = 9, hard_mode: bool = False) -> GameState:
    queue: List[GameState] = []
    heapq.heappush(queue, GameState(player_hp, player_mana, boss_hp, boss_dmg))

    while queue:
        current_frame = heapq.heappop(queue)
        for spell in current_frame.available_spells():
            next_frame = current_frame.copy()
            next_frame.player_hp -= 1 if hard_mode else 0
            if next_frame.player_hp <= 0:
                continue
            next_frame.cast(spell)
            next_frame.process_effects()
            if next_frame.boss_hp <= 0:
                return next_frame
            next_frame.boss_attack()
            if next_frame.player_hp <= 0:
                continue
            next_frame.process_effects()
            if next_frame.boss_hp <= 0:
                return next_frame
            heapq.heappush(queue, next_frame)


def load_data(input_file: str) -> Tuple[int, int]:
    with open(input_file) as f:
        return int(f.readline().strip().split()[-1]), int(f.readline().strip().split()[-1])


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    boss_hp, boss_dmg = load_data(input_file)
    final_frame = optimal_spells(boss_hp=boss_hp, boss_dmg=boss_dmg)
    return final_frame.mana_spent


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    boss_hp, boss_dmg = load_data(input_file)
    final_frame = optimal_spells(boss_hp=boss_hp, boss_dmg=boss_dmg, hard_mode=True)
    return final_frame.mana_spent


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
