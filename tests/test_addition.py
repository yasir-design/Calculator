"""This is the starting test file"""
from app.operations import addition


def test_addition():
    """Add Two Numbers"""
    assert addition(2, 2) == 4, "Addition is not working"
