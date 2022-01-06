"""
Advent of Code 2015 - Day 01
https://adventofcode.com/2015/day/1
"""

from itertools import accumulate, takewhile, tee
from pathlib import Path
from typing import Tuple

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def count_floors(directions: str) -> Tuple[int, int]:
    iterators = tee([-1 if _ == ')' else 1 for _ in directions], 2)
    final = sum(iterators[0])
    basement = 1 + sum([1 for _ in 
        takewhile(lambda x: x > -1, accumulate(iterators[1]))])
    return final, basement


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1_and_part2(input_file: str = DEFAULT_INPUT_FILE):
    part1, part2 =  count_floors(load_data(input_file))
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == '__main__':
    part1_and_part2()
