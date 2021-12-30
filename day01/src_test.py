import day01.src as src


def test_count_floors_part_1():
    assert src.count_floors('(())')[0] == 0
    assert src.count_floors('()()')[0] == 0
    assert src.count_floors('(((')[0] == 3
    assert src.count_floors('(()(()(')[0] == 3
    assert src.count_floors('))(((((')[0] == 3
    assert src.count_floors('())')[0] == -1
    assert src.count_floors('))(')[0] == -1
    assert src.count_floors(')))')[0] == -3
    assert src.count_floors(')())())')[0] == -3


def test_count_floors_part_2():
    assert src.count_floors(')')[1] == 1
    assert src.count_floors('()())')[1] == 5


def test_part1_and_part2():
    part1, part2 = src.count_floors(src.load_data(src.FULL_INPUT_FILE))
    assert part1 == 232
    assert part2 == 1783
