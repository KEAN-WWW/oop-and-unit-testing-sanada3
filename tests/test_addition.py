"""this is a starting test file"""

from app.calculator import add

def test_addition():
    """add two numbers"""
    # Test positive numbers
    assert add(2, 3) == 5
    # Test negative numbers
    assert add(-1, -1) == -2
    # Test with zero
    assert add(0, 5) == 5
