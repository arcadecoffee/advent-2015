"""
Advent of Code 2015 - Day 20
https://adventofcode.com/2015/day/20
"""

import itertools
import math
import pathlib

from typing import Set

__mypath = pathlib.Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> int:
    with open(input_file) as f:
        return int(f.readline().strip())


def get_gift_count(house_number: int, gift_factor: int = 10) -> int:
    divisor_sum = 0
    for i in range(1, math.ceil(math.sqrt(house_number))):
        if house_number % i == 0:
            divisor_sum += i + (house_number / i)
    divisor_sum += math.sqrt(house_number) if math.sqrt(house_number) % 1 else 0
    return divisor_sum * gift_factor


def get_gift_count_2(house_number: int, gift_factor: int = 11) -> int:
    divisor_sum = 0
    for i in range(1, math.ceil(math.sqrt(house_number))):
        if house_number % i == 0:
            divisor_sum += (house_number / i) + (i if house_number / i <= 50 else 0)
    divisor_sum += math.sqrt(house_number) if math.sqrt(house_number) % 1 else 0
    return divisor_sum * gift_factor


def part1(input_file: str = DEFAULT_INPUT_FILE):
    target = load_data(input_file)
    for i in itertools.count(1):
        if get_gift_count(i) >= target:
            return i


def part2(input_file: str = DEFAULT_INPUT_FILE):
    target = load_data(input_file)
    for i in itertools.count(1):
        if get_gift_count_2(i) >= target:
            return i


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
