import day18.src as src


def test_part1():
    assert src.part1(src.TEST1_INPUT_FILE, 4) == 4


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 768


def test_part2():
    assert src.part2(src.TEST2_INPUT_FILE, 5) == 17


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 781
