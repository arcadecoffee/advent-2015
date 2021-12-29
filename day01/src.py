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
    floors = []
    current_floor = 0
    for c in directions:
        current_floor += 1 if c == '(' else -1
        floors.append(current_floor)
    return floors


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1(input_file: str = DEFAULT_INPUT_FILE):
    return count_floors(load_data(input_file))[-1]


def part2(input_file: str = DEFAULT_INPUT_FILE):
    return count_floors(load_data(input_file)).index(-1) + 1


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 1: {part2()}')
