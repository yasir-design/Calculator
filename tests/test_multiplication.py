"""This is the starting test file"""
from app.operations import multiplication


def test_multiplication():
    """test multiplication"""
    assert multiplication(2, 2) == 4
