"""this is a starting test file"""

from app.calculator import multiply
def test_multiplication():
    """Test positive numbers"""
    assert multiply(2, 3) == 6
    #Test negative with positive
    assert multiply(-2, 3) == -6
    #Test with zero
    assert multiply(5, 0) == 0
