"""
Advent of Code 2015 - Day ZZ
https://adventofcode.com/2015/day/ZZ
"""

from hashlib import md5
from itertools import count
from pathlib import Path

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def find_number(secret_key: str, num_zeroes: int = 5):
    prefix = '0' * num_zeroes
    counter = count()
    n = next(counter)
    while not md5((secret_key + str(n)).encode()).hexdigest().startswith(prefix):
        n = next(counter)
    return n


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1(input_file: str = DEFAULT_INPUT_FILE):
    return find_number(load_data(input_file))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    return find_number(load_data(input_file), 6)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
