"""
Advent of Code 2015 - Day 19
https://adventofcode.com/2015/day/19
"""

from itertools import chain, permutations
from pathlib import Path
from typing import List, Tuple

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> Tuple[str, List[List[str]]]:
    replacements = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines[:-2]:
            replacements.append(line.strip().split(' => '))
        return lines[-1].strip(), replacements


def expand_molecule(molecule, replacements):
    new_molecules = []
    for r_in, r_out in replacements:
        moles = molecule.split(r_in)
        new_molecules += \
            [''.join(list(chain(*zip(moles, nm))) + [moles[-1]]) for nm in
             [[r_in] * i + [r_out] + [r_in] * (len(moles) - 2 - i) for i in range(len(moles) - 1)]]
    return new_molecules


def part1(input_file: str = DEFAULT_INPUT_FILE):
    molecule, replacements = load_data(input_file)
    new_molecules = expand_molecule(molecule, replacements)
    return len(set(new_molecules))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    data = load_data(input_file)
    return -1


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
