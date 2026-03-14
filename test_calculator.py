import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10

def test_multiply():
    # This will fail because multiply is buggy
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5.0
    
    # This will fail because divide doesn't raise ValueError on zero division
    with pytest.raises(ValueError):
        divide(5, 0)
