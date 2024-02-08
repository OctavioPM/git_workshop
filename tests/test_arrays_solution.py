from tutorial.arrays_solution import min_max


def test_min_max() -> None:
    assert min_max(range(10)) == (0, 9)
    assert min_max((7, 4, 2, 8, 1, 3)) == (1, 8)
    assert min_max([1]) == (1, 1)
