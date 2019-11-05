import Calculators
from Calculators.PopulationMean import population_mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def pop_mean(self, data):
        self.result = Calculators.population_mean(data)
        return self.result

    def med(self, data):
        self.result = Calculators.median(data)
        return self.result

    def z_score(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)
