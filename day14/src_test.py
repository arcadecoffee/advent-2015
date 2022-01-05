import day14.src as src


def test_run_race():
    results = src.run_race(src.load_data(src.TEST_INPUT_FILE), 1000)
    assert results['Comet'] == 1120
    assert results['Dancer'] == 1056


def test_part1():
    assert src.part1(src.TEST_INPUT_FILE, 1000) == 1120


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 2696


def test_score_race():
    results = src.score_race(src.load_data(src.TEST_INPUT_FILE), 1000)
    assert results['Comet'] == 312
    assert results['Dancer'] == 689


def test_part2():
    assert src.part2(src.TEST_INPUT_FILE, 1000) == 689


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 1084
