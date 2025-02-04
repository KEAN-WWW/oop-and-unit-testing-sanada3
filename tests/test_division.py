import pytest
def test_division():
    from app.calculator import divide
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3

def test_divide_zero_exception():
    from app.calculator import divide
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)