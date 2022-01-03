"""
Advent of Code 2015 - Day 8
https://adventofcode.com/2015/day/8
"""

import re

from pathlib import Path
from typing import List

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def decode_string(s: str) -> str:
    translations = {
        r'\\\\': '\\',
        r'\\"': '"',
        r'\\x..': lambda l: chr(int(l.group(0)[2:], 16))
    }
    return re.compile('|'.join(translations.keys())).sub(
        lambda l: translations[r'\\x..'](l) if l.group(0).startswith('\\x') else
        translations[re.escape(l.group(0))], s[1:-1])


def encode_string(s: str) -> str:
    translations = {
        r'\\': '\\\\',
        r'"': '\\"',
    }
    return '"' + re.compile('|'.join(translations.keys())).sub(
        lambda l: translations[re.escape(l.group(0))], s) + '"'


def load_data(input_file: str) -> List[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    raw_size = decoded_size = 0
    for s in load_data(input_file):
        raw_size += len(s)
        decoded_size += len(decode_string(s))
    return raw_size - decoded_size


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    raw_size = encoded_size = 0
    for s in load_data(input_file):
        raw_size += len(s)
        encoded_size += len(encode_string(s))
    return encoded_size - raw_size


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
