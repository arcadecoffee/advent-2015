"""
Advent of Code 2015 - Day 11
https://adventofcode.com/2015/day/11
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


def next_password(password: str) -> str:
    while True:
        password = \
            re.sub(r'([^z])(z*)([^z]?)$',
                   lambda l: (chr(ord(l.groups()[0]) + 1) if l.groups()[1] and
                                                             not l.groups()[2] else l.groups()[0]) +
                             ('a' * len(l.groups()[1]) if not l.groups()[2] else l.groups()[1]) +
                             (chr(ord(l.groups()[2]) + 1) if l.groups()[2] else ''),
                   password)

        password = re.sub(r'([ilo])(.*)$', lambda l: chr(ord(l.groups()[0]) + 1) +
                                                     ('a' * len(l.groups()[1])),
                          password)

        if (re.search(r'(\w)\1.*(\w)\2', password) and
                any([ord(password[i]) == ord(password[i + 1]) - 1 and
                     ord(password[i + 1]) == ord(password[i + 2]) - 1
                     for i in range(len(password) - 2)])):
            return password


def part1_and_part2(input_file: str = DEFAULT_INPUT_FILE):
    p1 = next_password(load_data(input_file))
    p2 = next_password(p1)
    return p1, p2


if __name__ == '__main__':
    p1, p2 = part1_and_part2()
    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')
