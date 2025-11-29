import pytest
from calculator import Calculator, safe_divide

def test_add():
    calc = Calculator()
    assert calc.add(3, 7) == 10

def test_division():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_safe_divide_success():
    assert safe_divide(8, 2) == 4

def test_safe_divide_zero():
    assert safe_divide(8, 0) is None
