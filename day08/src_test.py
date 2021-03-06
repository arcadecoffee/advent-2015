import day08.src as src


def test_part1():
    assert src.part1(src.TEST_INPUT_FILE) == 12


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 1350


def test_part2():
    assert src.part2(src.TEST_INPUT_FILE) == 19


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 2085
