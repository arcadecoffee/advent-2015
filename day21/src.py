"""
Advent of Code 2015 - Day 21
https://adventofcode.com/2015/day/21
"""

import collections
import itertools
import math
import pathlib

from typing import List

__mypath = pathlib.Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


Item = collections.namedtuple('Item', 'name cost damage armor')

WEAPONS = [
    Item('None', 0, 0, 0),
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0),
]

ARMOR = [
    Item('None', 0, 0, 0),
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5),
]

RINGS = [
    Item('None', 0, 0, 0),
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3),
]

RING_COMBOS = [(RINGS[0], RINGS[0])] + list(itertools.combinations(RINGS, 2))

def load_data(input_file: str) -> List[int]:
    with open(input_file) as f:
        return [int(l.strip().split(' ')[-1]) for l in f]


def find_cheapest_wardrobe(boss_hp, boss_damage, boss_armor, player_hp):
    lowest_cost = None
    for gear in itertools.product(WEAPONS, ARMOR, RING_COMBOS):
        gear_cost, player_damage, player_armor = (
            sum(i) for i in list(zip(gear[0], gear[1], *gear[2]))[1:])
        boss_win_rounds = math.ceil(player_hp / max(1, boss_damage - player_armor))
        player_win_rounds = math.ceil(boss_hp / max(1, player_damage - boss_armor))
        if player_win_rounds <= boss_win_rounds and (not lowest_cost or gear_cost < lowest_cost):
            lowest_cost = gear_cost
    return lowest_cost


def part1(input_file: str = DEFAULT_INPUT_FILE, player_hp: int = 100) -> int:
    data = load_data(input_file)
    lowest_cost = find_cheapest_wardrobe(*data, player_hp)
    return lowest_cost


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    data = load_data(input_file)
    return -1


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
