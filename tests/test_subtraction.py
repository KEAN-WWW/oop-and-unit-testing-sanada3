import pytest
def test_subtraction():
    from app.calculator import subtract
    # Test positive numbers
    assert subtract(5, 3) == 2
    # Test negative numbers
    assert subtract(-2, -3) == 1
    # Test with zero
    assert subtract(5, 0) == 5