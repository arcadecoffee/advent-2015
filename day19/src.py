"""
Advent of Code 2015 - Day 19
https://adventofcode.com/2015/day/19
"""

import re

from itertools import chain
from pathlib import Path
from typing import List, Tuple

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> Tuple[str, List[Tuple[str, ...]]]:
    transformations = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines[:-2]:
            transformations.append(tuple(line.strip().split(' => ')))
        return lines[-1].strip(), transformations


def get_new_molecules(molecule: str, transformations: List[Tuple[str, ...]]) -> List[str]:
    new_molecules = []
    for r_in, r_out in transformations:
        moles = molecule.split(r_in)
        new_molecules += \
            [''.join(list(chain(*zip(moles, nm))) + [moles[-1]]) for nm in
             [[r_in] * i + [r_out] + [r_in] * (len(moles) - 2 - i) for i in range(len(moles) - 1)]]
    return new_molecules


def reduce_molecule(molecule: str, electron_size: int) -> int:
    molecule = re.sub(r'[A-Z][a-z]?',
                      lambda l: '-' if l.group() not in ('Rn', 'Ar', 'Y') else l.group(),
                      molecule)
    steps = 1
    while len(molecule) > electron_size:
        molecule, n = re.subn('--', '-', molecule)
        molecule, m = re.subn('-Rn-(Y-)*Ar', '-', molecule)
        steps += n + m
    return steps


def part1(input_file: str = DEFAULT_INPUT_FILE):
    molecule, transformations = load_data(input_file)
    new_molecules = get_new_molecules(molecule, transformations)
    return len(set(new_molecules))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    molecule, transformations = load_data(input_file)
    electron_size = min([len(x[1]) for x in transformations if x[0] == 'e'])
    return reduce_molecule(molecule, electron_size)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
