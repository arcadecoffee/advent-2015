"""
Advent of Code 2015 - Day 25
https://adventofcode.com/2015/day/25
"""

import math
import pathlib
import re

from typing import Tuple

__mypath = pathlib.Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> Tuple[int, int]:
    with open(input_file) as f:
        row, column = (int(i) for i in re.search(r'row (\d+), column (\d+)', f.readline()).groups())
        return row, column


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    row, column = load_data(input_file)
    x = 20151125
    y = 252533
    z = 33554393
    t = row + column - 2
    e = (t * (t + 1) // 2) + column - 1
    code = (pow(y, e, z) * x) % z
    return code


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
