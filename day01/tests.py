from .src import part1, part2, count_floors, FULL_INPUT_FILE, TEST_INPUT_FILE


def test_count_floors_part_1():
    assert count_floors('(())')[-1] == 0
    assert count_floors('()()')[-1] == 0
    assert count_floors('(((')[-1] == 3
    assert count_floors('(()(()(')[-1] == 3
    assert count_floors('))(((((')[-1] == 3
    assert count_floors('())')[-1] == -1
    assert count_floors('))(')[-1] == -1
    assert count_floors(')))')[-1] == -3
    assert count_floors(')())())')[-1] == -3


def test_count_floors_part_2():
    assert count_floors(')').index(-1) + 1 == 1
    assert count_floors('()())').index(-1) + 1 == 5


def test_part1():
    assert part1(FULL_INPUT_FILE) == 232


def test_part2():
    assert part2(FULL_INPUT_FILE) == 1783
