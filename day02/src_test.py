import day02.src as src


def test_supplies_needed():
    assert src.paper_needed((2, 3, 4)) == 58
    assert src.paper_needed((1, 1, 10)) == 43


def test_ribbon_needed():
    assert src.ribbon_needed((2, 3, 4)) == 34
    assert src.ribbon_needed((1, 1, 10)) == 14


def test_part1_and_part2():
    assert src.part1_and_part2(src.TEST_INPUT_FILE) == (58 + 43, 34 + 14)


def test_part1_and_part2_full():
    assert src.part1_and_part2(src.FULL_INPUT_FILE) == (1606483, 3842356)
