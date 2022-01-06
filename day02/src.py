"""
Advent of Code 2015 - Day 02
https://adventofcode.com/2015/day/2
"""

from math import prod
from itertools import combinations, tee
from pathlib import Path
from typing import List, Tuple, Any, Generator

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> List[List[int]]:
    with open(input_file) as f:
        return [[int(i) for i in line.strip().split('x')] for line in f]


def paper_needed(dimensions: List[int]) -> int:
    a, b = tee([prod(i) for i in combinations(dimensions, 2)], 2)
    return 2 * sum(a) + min(b)


def ribbon_needed(dimensions: List[int]) -> int:
    return 2 * min(sum(i) for i in combinations(dimensions, 2)) + prod(dimensions)


def supplies_needed(dimensions: List[int]) -> Tuple[int, int]:
    return paper_needed(dimensions), ribbon_needed(dimensions)


def part1_and_part2(input_file: str = DEFAULT_INPUT_FILE):
    return tuple(sum(s) for s in
                 zip(*(supplies_needed(package) for package in load_data(input_file))))


if __name__ == '__main__':
    result = part1_and_part2()
    print(f'Part 1: {result[0]}')
    print(f'Part 2: {result[1]}')
