"""
Advent of Code 2015 - Day 7
https://adventofcode.com/2015/day/7
"""

from pathlib import Path
from typing import List

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


class Circuit:

    def __init__(self):
        self._wires = {}

        self._operation_map = {
            'AND': lambda l, r: self.wire(l) & self.wire(r),
            'OR': lambda l, r: self.wire(l) | self.wire(r),
            'LSHIFT': lambda l, r: self.wire(l) << self.wire(r),
            'RSHIFT': lambda l, r: self.wire(l) >> self.wire(r),
        }

    def process_instruction(self, instruction: str):
        left, right = instruction.split(' -> ')
        self._wires[right] = left

    def wire(self, wire_id: str):
        if wire_id.isdigit():
            return int(wire_id)
        elif type(self._wires[wire_id]) == int:
            return self._wires[wire_id]
        else:
            parts = self._wires[wire_id].split(' ')
            if len(parts) == 1:
                self._wires[wire_id] = self.wire(parts[0])
            elif len(parts) == 2:
                self._wires[wire_id] = ~ self.wire(self._wires[wire_id].split(' ')[1]) + (1 << 16)
            elif len(parts) == 3:
                self._wires[wire_id] = self._operation_map[parts[1]](parts[0], parts[2])
            return int(self._wires[wire_id])


def load_data(input_file: str) -> List[str]:
    with open(input_file) as f:
        return [line.strip() for line in f]


def build_circuit(instructions: List[str]) -> Circuit:
    c = Circuit()
    for instruction in instructions:
        c.process_instruction(instruction)
    return c


def part1(input_file: str = DEFAULT_INPUT_FILE):
    c = build_circuit(load_data(input_file))
    return c.wire('a')


def part2(input_file: str = DEFAULT_INPUT_FILE):
    c = build_circuit(load_data(input_file))
    c._wires['b'] = '956'
    return c.wire('a')


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
