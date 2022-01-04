"""
Advent of Code 2015 - Day 12
https://adventofcode.com/2015/day/12
"""

import json
from pathlib import Path
from typing import Dict, List, Union

__mypath = Path(__file__).resolve().parent
DEFAULT_INPUT_FILE = __mypath / 'input.full.txt'


def sum_numbers(data: Union[Dict, List], skip_red: bool = False) -> int:
    total = 0
    for item in data if type(data) == list \
            else data.values() if type(data) == dict and not (skip_red and 'red' in data.values()) \
            else []:
        total += item if type(item) == int else sum_numbers(item, skip_red)
    return total


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    return sum_numbers(json.load(open(input_file)))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    return sum_numbers(json.load(open(input_file)), True)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
