"""
Advent of Code 2015 - Day 13
https://adventofcode.com/2015/day/13
"""

import re

from collections import defaultdict
from itertools import permutations
from pathlib import Path
from typing import Dict

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> Dict[str, Dict[str, int]]:
    with open(input_file) as f:
        data = defaultdict(dict)
        for line in f:
            fields = re.match(r'(\w+) would (\w+) (\d+) .* (\w+)\.', line).groups()
            data[fields[0]][fields[3]] = (-1 if fields[1] == 'lose' else 1) * int(fields[2])
        return dict(data)


def optimize_table(data: Dict[str, Dict[str, int]]):
    def left(n: int, size: int):
        return (n + 1) if n < (size - 1) else 0

    def right(n: int, size: int):
        return (n - 1) if n > 0 else (size - 1)

    best = 0
    for s in permutations(list(data)[1:], len(data) - 1):
        s += list(data)[0],
        curr = sum([data[s[i]][s[left(i, len(s))]] + data[s[i]][s[right(i, len(s))]]
                    for i in range(len(s))])
        best = curr if curr > best else best
    return best


def part1(input_file: str = DEFAULT_INPUT_FILE):
    return optimize_table(load_data(input_file))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    data = load_data(input_file)
    data = {k: {**data[k], **{'me': 0}} for k in data}
    data['me'] = {k: 0 for k in data}
    return optimize_table(data)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
