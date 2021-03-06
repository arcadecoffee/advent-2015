import day09.src as src


def test_part1():
    assert src.part1(src.TEST_INPUT_FILE) == 605


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 251


def test_part2():
    assert src.part2(src.TEST_INPUT_FILE) == 982


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 898
