# Importing math module for square_root
import math
from Calculators.ZScore import zscore

# defining the functions to be used in Statistics Class


# Creating class calculator with mathematical functions
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

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)
