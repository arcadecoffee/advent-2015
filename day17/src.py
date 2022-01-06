"""
Advent of Code 2015 - Day 17
https://adventofcode.com/2015/day/17
"""

from itertools import chain, combinations
from pathlib import Path
from typing import List

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def get_combinations(containers: List[int], total_capacity: int = 150) -> List[List[int]]:
    return [g for g in [n for n in chain(*[combinations(containers, i)
                                           for i in range(1, len(containers) + 1)])]
            if sum(g) == total_capacity]


def load_data(input_file: str) -> List[int]:
    with open(input_file) as f:
        return [int(_.strip()) for _ in f]


def part1(input_file: str = DEFAULT_INPUT_FILE, total_capacity: int = 150):
    container_combinations = get_combinations(load_data(input_file), total_capacity)
    return len(container_combinations)


def part2(input_file: str = DEFAULT_INPUT_FILE, total_capacity: int = 150):
    container_combinations = get_combinations(load_data(input_file), total_capacity)
    min_containers = min([len(c) for c in container_combinations])
    return len([c for c in container_combinations if len(c) == min_containers])


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
