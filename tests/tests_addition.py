def test_addition():
    from app.calculator import add
    # Test positive numbers
    assert add(2, 3) == 5
    # Test negative numbers
    assert add(-1, -1) == -2
    # Test with zero
    assert add(0, 5) == 5