"""Do not change these tests, they are meant to check your code and should fail"""

from app.calculator import Calculator
from app.conversions import Convert


def test_calculator_operations():
    """Basic Calculator Tests using the Instance"""
    my_values = Convert.args_to_tuple(2, 2, 2)
    Calculator.add(my_values)
    assert Calculator.history.get_last_result() == 6, "The Addition Function Failed"
    Calculator.divide(my_values)
    assert Calculator.history.get_last_result() == .5, "The Division Function Failed"
    Calculator.multiply(my_values)
    assert Calculator.history.get_last_result() == 8, "Multiplication Didn't work"
    Calculator.subtract(my_values)
    assert Calculator.history.get_last_result() == -2, "Multiplication Didn't work"
