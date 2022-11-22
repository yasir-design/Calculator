"""This is the calculation class """
import pytest

from app.calculations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot
from app.conversions import Convert
from app.exceptions import OnlyOneValue


def test_addition_calculation():
    """Add Two Numbers"""
    # notice that each instance is independent of each other
    my_values = Convert.args_to_tuple(2, 2)
    addition_instance_1 = Addition.create(my_values)
    addition_instance_2 = Addition.create(Convert.args_to_tuple(3, 3))
    assert isinstance(addition_instance_1, Addition), "Is not a Addition Instance"
    assert isinstance(addition_instance_2, Addition), "Is not a Addition Instance"
    assert addition_instance_1.get_result() == 4, "Addition is not working"
    assert addition_instance_2.get_result() == 6, "Addition is not working"


def test_subtraction_calculation():
    """Subtract Two Numbers"""
    # notice that each instance is independent of each other
    subtraction_instance_1 = Subtraction.create((2, 2))
    subtraction_instance_2 = Subtraction.create((3, 2))
    assert isinstance(subtraction_instance_1, Subtraction), "Not a Subtraction Instance"
    assert isinstance(subtraction_instance_2, Subtraction), "Not a Subtraction Instance"
    assert subtraction_instance_1.get_result() == 0, "Subtraction is not working"
    assert subtraction_instance_2.get_result() == 1, "Subtraction is not working"


def test_multiplication_calculation():
    """Multiply Two Numbers"""
    # notice that each instance is independent of each other
    multiplication_instance_1 = Multiplication.create((2, 2))
    multiplication_instance_2 = Multiplication.create((3, 2))
    assert isinstance(multiplication_instance_1, Multiplication), "Not a Multiplication Instance"
    assert isinstance(multiplication_instance_2, Multiplication), "Not a Multiplication Instance"
    assert multiplication_instance_1.get_result() == 4, "Multiplication is not working"
    assert multiplication_instance_2.get_result() == 6, "Multiplication is not working"


def test_division_calculation():
    """Divide Two Numbers"""
    # pylint: disable=expression-not-assigned
    # notice that each instance is independent of each other
    my_tuple = (2, 2)
    division_instance_1 = Division.create(my_tuple)
    my_tuple = (3, 2)
    division_instance_2 = Division.create(my_tuple)

    assert isinstance(division_instance_1, Division), "Not a Division Instance"
    assert isinstance(division_instance_1, Division), "Not a Division Instance"
    assert division_instance_1.get_result() == 1, "Division is not working"
    assert division_instance_2.get_result() == 1.5, "Division is not working"
    with pytest.raises(ZeroDivisionError):
        Division.create((3, 0)).get_result(), "Fails Divide By Zero"


def test_square_calculation():
    """Divide Two Numbers"""
    # notice that each instance is independent of each other
    my_float = 2.0
    square_instance_1 = Square.create(my_float)
    assert square_instance_1.get_result() == 4


def test_square_root_calculation():
    """Divide Two Numbers"""
    # notice that each instance is independent of each other
    my_float = 4.0
    square_root_instance_1 = SquareRoot.create(my_float)
    assert square_root_instance_1.get_result() == 2


def test_only_one_value_exception():
    """Checking Exception"""
    # pylint: disable=expression-not-assigned
    my_value = 1
    with pytest.raises(OnlyOneValue):
        Subtraction.create(my_value).get_result() == 2
