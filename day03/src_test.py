import day03.src as src


def test_count_stops():
    assert src.count_stops('>') == 2
    assert src.count_stops('^>v<') == 4


def test_part1():
    assert src.part1(src.TEST_INPUT_FILE) == 2


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 2565


def test_count_stops_part2():
    assert src.count_stops('^v', 2) == 3
    assert src.count_stops('^>v<', 2) == 3


def test_part2():
    assert src.part2(src.TEST_INPUT_FILE) == 11


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 2639
