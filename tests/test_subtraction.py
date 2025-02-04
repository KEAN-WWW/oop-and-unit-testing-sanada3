"""file for subtraction"""

from app.calculator import subtract
def test_subtraction():
    """subtract two numbers"""

    # Test positive numbers
    assert subtract(5, 3) == 2
    # Test negative numbers
    assert subtract(-2, -3) == 1
    # Test with zero
    assert subtract(5, 0) == 5
