"""
Advent of Code 2015 - Day 01
https://adventofcode.com/2021/day/01
"""

import sys
from pathlib import Path
file = Path(__file__).resolve()
sys.path.append(str(file.parent.parent))

import common
from typing import Tuple

FULL_INPUT_FILE = file.parent / 'input.full.txt'
TEST_INPUT_FILE = file.parent / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def count_floors(directions: str) -> Tuple[int, int]:
    basement = None
    current_floor = 0
    for i in range(len(directions)):
        current_floor += 1 if directions[i] == '(' else -1
        if not basement and current_floor == -1:
            basement = i + 1
        common.print_progress_bar(len(directions) - 1, i)
    return current_floor, basement


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1_and_part2(input_file: str = DEFAULT_INPUT_FILE):
    part1, part2 =  count_floors(load_data(input_file))
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == '__main__':
    part1_and_part2()
