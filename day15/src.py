"""
Advent of Code 2015 - Day 15
https://adventofcode.com/2015/day/15
"""

import re

from collections import defaultdict
from itertools import permutations
from math import prod
from pathlib import Path
from typing import Dict

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> Dict[str, Dict[str, int]]:
    data = {}
    with open(input_file) as f:
        for line in f:
            g = re.match(r'(\w+):' + r' (\w+) (-?\d+).*' * 5, line).groups()
            data[g[0]] = {g[i]: int(g[i + 1]) for i in range(1, len(g), 2)}
    return data


def calculate_recipes(ingredients: dict, qty: int):
    recipes = {}
    for p in [_ for _ in permutations(range(1, qty + 1), len(ingredients)) if sum(_) == qty]:
        recipes[p] = defaultdict(int)
        for ingredient, amount in zip(ingredients.keys(), p):
            for k, v in ingredients[ingredient].items():
                recipes[p][k] += v * amount
        recipes[p]['score'] = prod([max(v, 0) for k, v in recipes[p].items() if k != 'calories'])
    return recipes


def part1_and_part2(input_file: str = DEFAULT_INPUT_FILE):
    recipes = calculate_recipes(load_data(input_file), 100)
    p1 = recipes[max(recipes, key=lambda k: recipes[k]['score'])]['score']

    low_cal_recipes = {k: v for k, v in recipes.items() if v['calories'] == 500}
    p2 = low_cal_recipes[max(low_cal_recipes, key=lambda k: low_cal_recipes[k]['score'])]['score']

    return p1, p2


if __name__ == '__main__':
    print('Part 1: {}\nPart 2: {}'.format(*part1_and_part2()))
