import day10.src as src


def test_part1():
    assert len(src.look_and_say(src.load_data(src.TEST_INPUT_FILE), 5)) == 6


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 492982


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 6989950
