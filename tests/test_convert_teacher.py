""" This converts data """
from app.conversions import Convert


def test_calculator_operations():
    """checks that convert args to tuple works"""
    assert isinstance(Convert.args_to_tuple(2, 2, 2), tuple)
