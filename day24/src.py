"""
Advent of Code 2015 - Day 24
https://adventofcode.com/2015/day/24
"""

import itertools
import math
import pathlib

from typing import Dict, List

__mypath = pathlib.Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> List[int]:
    with open(input_file) as file:
        return list(reversed([int(line.strip()) for line in file]))


def has_valid_combo(items: List[int], target: int) -> bool:
    for set_size in range(1, len(items) - 1):
        for c in itertools.combinations(items, set_size):
            if sum(c) == target:
                return True
    return False


def find_good_combos(data: List[int], target: int):
    combos = []
    set_size = 1
    while not combos and set_size < len(data):
        for c in itertools.combinations(data, set_size):
            if sum(c) == target and has_valid_combo([d for d in data if d not in c], target):
                combos.append(c)
        set_size += 1
    return combos


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    data = load_data(input_file)
    good_combos = find_good_combos(data, int(sum(data) / 3))
    return min([math.prod(c) for c in good_combos])


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    data = load_data(input_file)
    return -1


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
