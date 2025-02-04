"""this is a starting test file"""
import pytest
from app.calculator import divide


def test_division():
    """division numbers"""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3


def test_divide_zero_exception():
    """divide two numbers"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
