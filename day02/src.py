"""
Advent of Code 2015 - Day 02
https://adventofcode.com/2021/day/02
"""

from pathlib import Path
from typing import Tuple

FULL_INPUT_FILE = Path(__file__).parent / 'input.full.txt'
TEST_INPUT_FILE = Path(__file__).parent / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def giftwrap_needed(data: str) -> Tuple[int, int]:
    return None, None


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1_and_part2(input_file: str = DEFAULT_INPUT_FILE):
    part1, part2 = giftwrap_needed(load_data(input_file))
    print(f'Part 1: {part1}')
    print(f'Part 1: {part2}')


if __name__ == '__main__':
    part1_and_part2()