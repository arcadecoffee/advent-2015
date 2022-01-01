"""
Advent of Code 2015 - Day ZZ
https://adventofcode.com/2015/day/ZZ
"""

import re
from pathlib import Path
from typing import List

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST1_INPUT_FILE = __mypath / 'input.test1.txt'
TEST2_INPUT_FILE = __mypath / 'input.test2.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def check_string(string: str, version: int = 1) -> bool:
    checks = {
        1: lambda s:
            len(re.findall(r'[aeiou]', s)) >= 3
            and re.search(r'(\w)\1', s) is not None
            and re.search(r'ab|cd|pq|xy', s) is None
        ,

        2: lambda s:
            re.search(r'(\w{2}).*\1', string) is not None
            and re.search(r'(\w)\w\1', s) is not None
        ,
    }
    return checks[version](string)


def count_valid_strings(strings: List[str], version: int = 1) -> int:
    count = 0
    for string in strings:
        count += 1 if check_string(string, version) else 0
    return count


def load_data(input_file: str) -> List[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def part1(input_file: str = DEFAULT_INPUT_FILE):
    return count_valid_strings(load_data(input_file))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    return count_valid_strings(load_data(input_file), 2)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
