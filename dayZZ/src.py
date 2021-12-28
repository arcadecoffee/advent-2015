"""
Advent of Code 2015 - Day ZZ
https://adventofcode.com/2021/day/ZZ
"""

from typing import List

FULL_INPUT_FILE = f'input.full.txt'
TEST_INPUT_FILE = f'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1(input_file: str = DEFAULT_INPUT_FILE):
    data = load_data(input_file)
    return 1


def part2(input_file: str = DEFAULT_INPUT_FILE):
    data = load_data(input_file)
    return 1


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 1: {part2()}')
