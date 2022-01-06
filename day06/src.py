"""
Advent of Code 2015 - Day 6
https://adventofcode.com/2015/day/6
"""

import re
from collections import defaultdict
from pathlib import Path
from typing import Generator, Tuple, Union

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


class LightGrid:
    def __init__(self, rows: int = 1000, cols: int = 1000, mode: int = 1):
        self.rows, self.cols = rows, cols
        self.mode = mode
        self.grid = defaultdict(lambda: defaultdict(int))
        self._action_map = {
            'turn on': self.turn_on,
            'turn off': self.turn_off,
            'toggle': self.toggle
        }

    def turn_on(self, x_start: int, y_start: int, x_end: int, y_end: int) -> None:
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                self.grid[x][y] = (self.grid[x][y] + 1) if self.mode == 2 else 1

    def turn_off(self, x_start: int, y_start: int, x_end: int, y_end: int) -> None:
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                self.grid[x][y] -= 1 if self.grid[x][y] > 0 else 0

    def toggle(self, x_start: int, y_start: int, x_end: int, y_end: int) -> None:
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                if self.mode == 2:
                    self.turn_on(x, y, x, y)
                    self.turn_on(x, y, x, y)
                else:
                    if not self.grid[x][y]:
                        self.turn_on(x, y, x, y)
                    else:
                        self.turn_off(x, y, x, y)

    def process_instruction(self, action: str, x_start: int, y_start: int, x_end: int, y_end: int)\
            -> None:
        self._action_map[action](x_start, y_start, x_end, y_end)

    @property
    def activated(self):
        return sum([sum(r.values()) for r in self.grid.values()])


def load_data(input_file: str) -> Generator[Tuple[Union[str, int]], str, None]:
    with open(input_file) as f:
        for line in f:
            fields = re.search(r'(.*) (\d*),(\d*) through (\d*),(\d*)', line).groups()
            yield fields[0], *(int(n) for n in fields[1:])


def part1(input_file: str = DEFAULT_INPUT_FILE) -> int:
    lg = LightGrid()
    for instruction in load_data(input_file):
        lg.process_instruction(*instruction)
    return lg.activated


def part2(input_file: str = DEFAULT_INPUT_FILE) -> int:
    lg = LightGrid(mode=2)
    for instruction in load_data(input_file):
        lg.process_instruction(*instruction)
    return lg.activated


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
