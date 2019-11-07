from Calculators.Calculator import Calculator
from Calculators.ZScore import zscore


class Statistics(Calculator):
    data = []

    def __init__(self):
        pass

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result
