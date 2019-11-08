from Calculators.Calculator import Calculator
from Statistics.ZScore import z_score
from Statistics.ConfidenceInterval import confidence_interval
from Statistics.PopulationVariance import population_variance
from Statistics.PopulationMean import population_mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.VariancePopulationProportion import var_pop_proportion

from CSVReader.CSVReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)

    def pop_mean(self):
        self.result = population_mean(self.data)
        return self.result

    def med(self):
        self.result = median(self.data)
        return self.result

    def mod(self):
        self.result = mode(self.data)
        return self.result

    def variance_pop_proportion(self):
        self.result = var_pop_proportion(self.data)
        return self.result

    def z_score(self):
        self.result = z_score(self.data)
        return self.result

    def confidence_interval(self):
        self.result = confidence_interval(self.data)
        return self.result

    def population_variance(self):
        self.result = population_variance(self.data)
        return self.result
