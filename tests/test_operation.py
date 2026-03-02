from src.maths_operations import add, subtract

def test_add():
    assert add(2, 4) == 6
    assert add(9, -1) == 8
    assert add(-2, -4) == -6

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(-1, -4) == 3
    assert subtract(-6, 10) == -16
