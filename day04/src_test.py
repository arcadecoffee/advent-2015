import day04.src as src


def test_find_number():
    assert src.find_number('abcdef') == 609043


def test_part1():
    assert src.part1(src.TEST_INPUT_FILE) == 1048970


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 117946


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 3938038
