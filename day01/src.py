"""
Advent of Code 2015 - Day 01
https://adventofcode.com/2021/day/01
"""

from pathlib import Path
from typing import List

FULL_INPUT_FILE = Path(__file__).parent / 'input.full.txt'
TEST_INPUT_FILE = Path(__file__).parent / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def count_floors(directions: str) -> List[int]:
    basement = None
    current_floor = 0
    for i in range(len(directions)):
        current_floor += 1 if directions[i] == '(' else -1
        if not basement and current_floor == -1:
            basement = i + 1
    return current_floor, basement


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1_and_part2(input_file: str = DEFAULT_INPUT_FILE):
    part1, part2 =  count_floors(load_data(input_file))
    print(f'Part 1: {part1}')
    print(f'Part 1: {part2}')


if __name__ == '__main__':
    part1_and_part2()