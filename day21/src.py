"""
Advent of Code 2015 - Day 21
https://adventofcode.com/2015/day/21
"""

import collections
import itertools
import pathlib

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


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    data = load_data(input_file)
    ring_combos = [(RINGS[0], RINGS[0])] + list(itertools.combinations(RINGS, 2))
    for wardrobe in itertools.product(WEAPONS, ARMOR, ring_combos):
        total_cost, total_damage, total_armor = (
            sum(i) for i in list(zip(wardrobe[0], wardrobe[1], *wardrobe[2]))[1:])


        x = 0
    return -1


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    data = load_data(input_file)
    return -1


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
