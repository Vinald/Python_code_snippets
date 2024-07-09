from summing import summing
import pytest

# using assert to test a function 
def test_positive():
    assert summing(1, 2) == 3
    assert summing(2, 2) == 4


def test_negative():
    assert summing(-1, 1) == 0
    assert summing(-1, -3) == -4


def test_zero():
    assert summing(0, 0) == 0


def test_str():
    with pytest.raises(TypeError):
        summing('string', 'string')
