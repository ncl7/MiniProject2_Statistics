from Calculators.Calculator import Calculator


class Statistics(Calculator):
    data = []

    def __init__(self):

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result
