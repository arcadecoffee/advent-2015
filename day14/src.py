"""
Advent of Code 2015 - Day 14
https://adventofcode.com/2015/day/14
"""

import re

from collections import defaultdict
from pathlib import Path
from typing import Any, Generator, List, Union, Dict

__mypath = Path(__file__).resolve().parent
FULL_INPUT_FILE = __mypath / 'input.full.txt'
TEST_INPUT_FILE = __mypath / 'input.test1.txt'
DEFAULT_INPUT_FILE = FULL_INPUT_FILE


def load_data(input_file: str) -> Dict[str, Dict[str, int]]:
    data = {}
    with open(input_file) as f:
        for line in f:
            name, speed, duration, rest = \
                (int(i) if i.isdigit() else i
                 for i in re.match(r'(\w+).* (\d+).* (\d+).* (\d+)', line).groups())
            data[name] = {'speed': speed, 'duration': duration, 'rest': rest}
    return data


def run_race(reindeer: Dict[str, Dict[str, int]], race_duration: int) -> Dict[str, int]:
    results = {}
    for k, v in reindeer.items():
        cycle = v['duration'] + v['rest']
        run_seconds = \
            (int(race_duration / cycle) * v['duration']) + min([v['duration'], race_duration % cycle])
        results[k] = v['speed'] * ((int(race_duration / cycle) * v['duration']) +
                                   min([v['duration'], race_duration % cycle]))
    return results


def score_race(reindeer: Dict[str, Dict[str, int]], race_duration: int) -> Dict[str, int]:
    results = defaultdict(int)
    for s in range(race_duration):
        split_results = run_race(reindeer, s + 1)
        for r in [r for r in split_results if split_results[r] == max(split_results.values())]:
            results[r] += 1
    return results


def part1(input_file: str = DEFAULT_INPUT_FILE, race_duration: int = 2503):
    return max(run_race(load_data(input_file), race_duration).values())


def part2(input_file: str = DEFAULT_INPUT_FILE, race_duration: int = 2503):
    return max(score_race(load_data(input_file), race_duration).values())


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
