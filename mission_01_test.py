from mission_01 import add

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negative_numbers():
    assert add(-1, 1) == 0
