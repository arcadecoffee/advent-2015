import day01.src as src

def test_count_floors_part_1():
    assert src.count_floors('(())')[-1] == 0
    assert src.count_floors('()()')[-1] == 0
    assert src.count_floors('(((')[-1] == 3
    assert src.count_floors('(()(()(')[-1] == 3
    assert src.count_floors('))(((((')[-1] == 3
    assert src.count_floors('())')[-1] == -1
    assert src.count_floors('))(')[-1] == -1
    assert src.count_floors(')))')[-1] == -3
    assert src.count_floors(')())())')[-1] == -3


def test_count_floors_part_2():
    assert src.count_floors(')').index(-1) + 1 == 1
    assert src.count_floors('()())').index(-1) + 1 == 5


def test_part1():
    assert src.part1(src.FULL_INPUT_FILE) == 232


def test_part2():
    assert src.part2(src.FULL_INPUT_FILE) == 1783
