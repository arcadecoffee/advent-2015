"""
Advent of Code 2015 - Day 16
https://adventofcode.com/2015/day/16
"""

from pathlib import Path

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> dict:
    with open(input_file) as f:
        return {
            s[:s.index(':')]: dict([(t.split(': ')[0], int(t.split(': ')[1]))
                                    for t in s[s.index(':') + 2:].split(', ')])
            for s in f
        }


def find_sue(data: dict) -> int:
    knowns = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    for fact, value in knowns.items():
        data = {k: v for k, v in data.items() if v.get(fact, value) == value}

    return int(list(data.keys())[0].split(' ')[1])


def find_real_sue(data: dict) -> int:
    knowns = {
        'children': 3,
        'samoyeds': 2,
        'akitas': 0,
        'vizslas': 0,
        'cars': 2,
        'perfumes': 1,
    }
    for fact, value in knowns.items():
        data = {k: v for k, v in data.items() if v.get(fact, value) == value}

    greater_thans = {
        'cats': 7,
        'trees': 3,
    }
    for fact, value in greater_thans.items():
        data = {k: v for k, v in data.items() if v.get(fact, value + 1) > value}

    less_thans = {
        'pomeranians': 3,
        'goldfish': 5,
    }
    for fact, value in less_thans.items():
        data = {k: v for k, v in data.items() if v.get(fact, value - 1) < value}

    return int(list(data.keys())[0].split(' ')[1])


def part1(input_file: str = DEFAULT_INPUT_FILE):
    return find_sue(load_data(input_file))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    return find_real_sue(load_data(input_file))


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
