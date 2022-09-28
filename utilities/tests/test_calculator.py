from utilities.calculator import *
import pytest


def test_add():
    assert add(0, 1) == 1


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(6, 3) == 18


def test_divide():
    assert divide(8, 4) == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


