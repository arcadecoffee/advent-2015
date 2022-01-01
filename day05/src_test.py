import day05.src as src


def test_check_string():
    tests = {
        'ugknbfddgicrmopn': True,
        'aaa': True,
        'jchzalrnumimnmhp': False,
        'haegwjzuvuyypxyu': False,
        'dvszwmarrgswjxmb': False
    }
    for t in tests:
        assert src.check_string(t) == tests[t]


def test_part1():
    assert src.part1(src.TEST1_INPUT_FILE) == 2


def test_part1_full():
    assert src.part1(src.FULL_INPUT_FILE) == 236


def test_check_string_2():
    tests = {
        'qjhvhtzxzqqjkmpb': True,
        'xxyxx': True,
        'uurcxstgmygtbstg': False,
        'ieodomkazucvgmuy': False
    }
    for t in tests:
        assert src.check_string(t, 2) == tests[t]


def test_part2():
    assert src.part2(src.TEST2_INPUT_FILE) == 2


def test_part2_full():
    assert src.part2(src.FULL_INPUT_FILE) == 51
