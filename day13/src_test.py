import day13.src as src


def test_part1():
    assert src.part1(src.TEST_INPUT_FILE) == 330


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 664


def test_part2():
    assert src.part2(src.TEST_INPUT_FILE) == 1


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 1
