import day15.src as src


def test_part1():
    assert src.part1_and_part2(src.TEST_INPUT_FILE)[0] == 62842880


def test_part1_full():
    assert src.part1_and_part2(src.FULL_INPUT_FILE)[0] == 18965440


def test_part2():
    assert src.part1_and_part2(src.TEST_INPUT_FILE)[1] == 57600000


def test_part2_full():
    assert src.part1_and_part2(src.FULL_INPUT_FILE)[1] == 15862900
