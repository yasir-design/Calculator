"""This is the starting test file"""
from app.operations import subtraction


def test_subtraction():
    """Subtraction"""

    assert subtraction(1, 1) == 0
