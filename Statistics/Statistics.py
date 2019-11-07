from Calculators.Calculator import Calculator
from Calculators.ZScore import zscore
from Calculators.ConfidenceInterval import confidence_interval

class Statistics(Calculator):
    data = []

    def __init__(self):
        pass

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result

    def confidence_interval(self, a):
        self.result = confidence_interval(a)
        return self.result

    def
