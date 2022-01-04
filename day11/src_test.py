import day11.src as src


def test_part1_1():
    assert src.next_password('abcdefgh') == 'abcdffaa'


def test_part1_and_part2():
    assert src.part1_and_part2(src.TEST_INPUT_FILE) == ('ghjaabcc', 'ghjbbcdd')


def test_part1_and_part2_full():
    assert src.part1_and_part2(src.FULL_INPUT_FILE) == ('cqjxxyzz', 'cqkaabcc')
