"""Calculations abstract class and concrete operations"""
import math

from app.operations import *
from app.exceptions import *


class Calculation(list):
    """My abstract Base Calculation Class"""

    @classmethod
    def create(cls, my_values):
        """Factory Method"""
        return cls(my_values)

    def __init__(self, my_values):
        """This is the base class constructor"""

        super().__init__()
        try:
            for value in my_values:
                self.append(value)
        except TypeError:
            self.append(my_values)

    def __repr__(self):
        values = ', '.join(str(x) for x in self)
        return f'Calculation Type: {type(self)}, values: {values}, result={self.get_result()})'

    def get_result(self):
        pass


class Addition(Calculation):
    """My Addition Concrete Calculation Class"""

    def get_result(self):
        sum_of_values = 0.0
        for val in self:
            sum_of_values = addition(sum_of_values, val)
        return sum_of_values


class Square(Calculation):
    """My square Concrete Calculation Class"""

    def get_result(self):
        return pow(self[0], 2)


class SquareRoot(Calculation):
    """My square root Concrete Calculation Class"""

    def get_result(self):
        return math.sqrt(self[0])


class Subtraction(Calculation):
    """My Subtraction Concrete Calculation Class"""

    def get_result(self):
        if len(self) == 1:
            raise OnlyOneValue
        difference_of_values = self[0]
        list_iterator = iter(self)
        next(list_iterator)
        for val in list_iterator:
            difference_of_values = subtraction(difference_of_values, val)
        return difference_of_values


class Division(Calculation):
    """My Division Concrete Calculation Class"""

    def get_result(self):
        quotient_of_values = self[0]
        list_iterator = iter(self)
        next(list_iterator)
        for val in list_iterator:
            quotient_of_values = division(quotient_of_values, val)
        return quotient_of_values


class Multiplication(Calculation):
    """My Multiplication Concrete Calculation Class"""

    def get_result(self):
        multiplication_of_values = self[0]
        list_iterator = iter(self)
        next(list_iterator)
        for val in list_iterator:
            multiplication_of_values = multiplication(multiplication_of_values, val)
        return multiplication_of_values
