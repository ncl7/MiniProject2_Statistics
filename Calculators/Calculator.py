from Calculators.Addition import addition
from Calculators.Subtraction import subtraction
from Calculators.Multiplication import multiplication
from Calculators.Division import division
from Calculators.SquareRoot import square_root
from Calculators.Squaring import square


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def squaring(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = square_root(a)
        return self.result
