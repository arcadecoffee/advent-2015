"""
Advent of Code 2015 - Day 9
https://adventofcode.com/2015/day/9
"""

import re

from collections import defaultdict
from pathlib import Path
from typing import Dict, List

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_routes(input_file: str) -> Dict[str, Dict[str, int]]:
    routes = defaultdict(dict)
    with open(input_file) as f:
        for line in f:
            a, b, distance = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()
            routes[a][b] = routes[b][a] = int(distance)
    return routes


def find_route(routes: Dict, visited: List = None, cost: int = 0, mode: callable = min) -> int:
    return mode([find_route(routes, [origin], mode=mode) for origin in routes]) if not visited \
        else mode([find_route(routes, visited + [destination],
                              cost + routes[visited[-1]][destination], mode=mode)
                   for destination in routes[visited[-1]] if destination not in visited] or [cost])


def part1(input_file: str = DEFAULT_INPUT_FILE):
    return find_route(load_routes(input_file))


def part2(input_file: str = DEFAULT_INPUT_FILE):
    return find_route(load_routes(input_file), mode=max)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
