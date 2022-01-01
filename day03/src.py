"""
Advent of Code 2015 - Day 03
https://adventofcode.com/2015/day/3
"""

from itertools import cycle
from pathlib import Path

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


class Coordinates:
    def __init__(self, x: int = 0, y: int = 0):
        self.x, self.y = x, y

    def __add__(self, other):
        return self.__class__(x=self.x + other.x, y=self.y + other.y)

    @property
    def coords(self):
        return self.x, self.y


def count_stops(directions: str, num_santas: int = 1) -> int:
    direction_to_coords = {
        '>': Coordinates(1, 0), '<': Coordinates(-1, 0),
        '^': Coordinates(0, 1), 'v': Coordinates(0, -1)
    }

    santas = []
    for n in range(num_santas):
        santas.append(Coordinates())
    stops = {santas[0].coords}
    santa_cycle = cycle(range(num_santas))

    for d in directions:
        santa = next(santa_cycle)
        santas[santa] += direction_to_coords[d]
        stops.add(santas[santa].coords)

    return len(stops)


def load_data(input_file: str) -> str:
    with open(input_file) as f:
        return f.readline().strip()


def part1(input_file: str = DEFAULT_INPUT_FILE):
    return count_stops(load_data(input_file))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    return count_stops(load_data(input_file), 2)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
