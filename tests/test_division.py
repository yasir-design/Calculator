"""This is the starting test file"""
import pytest
from app.operations import division


def test_division():
    """Divide Two Numbers"""
    assert division(2, 2) == 1


def test_divide_zero_exception():
    """Tests that division by zero exception is thrown"""
    with pytest.raises(ZeroDivisionError):
        division(4, 0)
