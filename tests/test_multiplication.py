def test_multiplication():
    from app.calculator import multiply
    # Test positive numbers
    assert multiply(2, 3) == 6
    # Test negative with positive
    assert multiply(-2, 3) == -6
    # Test with zero
    assert multiply(5, 0) == 0