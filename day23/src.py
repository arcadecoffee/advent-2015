"""
Advent of Code 2015 - Day 23
https://adventofcode.com/2015/day/23
"""

import pathlib
import re

from typing import Any, Dict, List

__mypath = pathlib.Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


class Computer:
    def __init__(self, a: int = 0, b: int = 0):
        self.registers: Dict[str, int] = {'a': a, 'b': b}

    def execute_instructions(self, instructions: List[List[Any]]):
        instruction_pointer: int = 0
        while instruction_pointer < len(instructions):
            curr = instructions[instruction_pointer]
            if curr[0] == 'jmp':
                instruction_pointer += curr[1]
            elif ((curr[0] == 'jio' and self.registers[curr[1]] == 1)
                  or (curr[0] == 'jie' and not (self.registers[curr[1]] % 2))):
                instruction_pointer += curr[2]
            else:
                if curr[0] == 'hlf':
                    self.registers[curr[1]] = int(self.registers[curr[1]] / 2)
                elif curr[0] == 'tpl':
                    self.registers[curr[1]] = self.registers[curr[1]] * 3
                elif curr[0] == 'inc':
                    self.registers[curr[1]] = self.registers[curr[1]] + 1
                instruction_pointer += 1


def load_data(input_file: str) -> List[List[Any]]:
    with open(input_file) as f:
        data = [l.strip() for l in f]
        data = [re.split(' |, ', d) for d in data]
        return [[int(f) if not f.isalpha() else f for f in d] for d in data]


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    data = load_data(input_file)
    c = Computer()
    c.execute_instructions(data)
    return c.registers['b']


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    data = load_data(input_file)
    c = Computer(a=1)
    c.execute_instructions(data)
    return c.registers['b']


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
