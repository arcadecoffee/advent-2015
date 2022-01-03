"""
Advent of Code 2015 - Day 10
https://adventofcode.com/2015/day/10
"""

import re

from pathlib import Path

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def look_and_say(look: str, cycles: int = 5):
    for _ in range(cycles):
        say = ''
        offset = 0
        while offset < len(look):
            print(f'\r{_}: {len(look) - offset}', end='')
            end = re.match(r'^(.)\1*', look[offset:]).end()
            say += f'{end}{look[offset]}'
            offset += end
        look = say
    print('\r', end='')
    return look


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    return len(look_and_say(load_data(input_file), 40))


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    return len(look_and_say(load_data(input_file), 50))


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
