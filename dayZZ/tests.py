from .src import part1, part2, FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part1():
    assert part1(TEST_INPUT_FILE) == 0


def test_part1_full():
    assert part2(FULL_INPUT_FILE) == 0


def test_part2():
    assert part2(TEST_INPUT_FILE) == 0


def test_part2_full():
    assert part2(FULL_INPUT_FILE) == 0
