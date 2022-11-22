"""Calculator Class"""
from app.calculations import *
from app.history import CalculationHistoryList as History


class Calculator:
    """Improved Calculator with Class Methods and using the calculation history static prop instance"""
    # this is  a static history property holding our history list class
    history = History()

    @classmethod
    def add(cls, my_values: tuple):
        return cls.history.append(Addition.create(my_values))

    @classmethod
    def divide(cls, my_values: tuple):
        return cls.history.append(Division.create(my_values))

    @classmethod
    def multiply(cls, my_values: tuple):
        return cls.history.append(Multiplication.create(my_values))

    @classmethod
    def subtract(cls, my_values: tuple):
        return cls.history.append(Subtraction.create(my_values))
