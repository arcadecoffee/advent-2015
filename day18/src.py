"""
Advent of Code 2015 - Day 18
https://adventofcode.com/2015/day/18
"""

from itertools import product
from pathlib import Path
from typing import List, Tuple

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST1_INPUT_FILE = __mypath / 'input.test1.txt'
TEST2_INPUT_FILE = __mypath / 'input.test2.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


class LightGrid:
    def __init__(self, initial_grid: List[List[bool]], stuck_corners: bool = False):
        self.grid = initial_grid
        self.width = len(initial_grid)
        self.height = len(initial_grid[0])
        self.stuck_corners = stuck_corners

    def neighbors(self, r: int, c: int) -> List[Tuple[int, int]]:
        return [p for p in (product((r - 1, r, r + 1), (c - 1, c, c + 1))) if
                self.width > p[0] >= 0 and self.height > p[1] >= 0 and
                not (p[0] == r and p[1] == c)]

    def neighbors_on(self, r: int, c: int):
        return sum([self.grid[n[0]][n[1]] for n in self.neighbors(r, c)])

    def cycle(self, num: int) -> None:
        for _ in range(num):
            self.grid = \
                [[(self.grid[r][c] and self.neighbors_on(r, c) == 2)
                  or self.neighbors_on(r, c) == 3 for c in range(self.width)]
                 for r in range(self.height)]
            if self.stuck_corners:
                self.grid[0][0] = self.grid[0][-1] = self.grid[-1][0] = self.grid[-1][-1] = True

    @property
    def lights_on(self) -> int:
        return sum([sum(r) for r in self.grid])


def load_data(input_file: str) -> List[List[bool]]:
    with open(input_file) as f:
        return [[c == '#' for c in s.strip()] for s in f]


def part1(input_file: str = DEFAULT_INPUT_FILE, steps: int = 100):
    lg = LightGrid(load_data(input_file))
    lg.cycle(steps)
    return lg.lights_on


def part2(input_file: str = DEFAULT_INPUT_FILE, steps: int = 100):
    lg = LightGrid(load_data(input_file), True)
    lg.cycle(steps)
    return lg.lights_on


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
