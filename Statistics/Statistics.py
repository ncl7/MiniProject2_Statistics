from Calculators.Calculator import Calculator
from Statistics.ZScore import z_score
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.ConfidenceInterval import confidence_interval
from Statistics.PopulationVariance import population_variance
from Statistics.PopulationMean import population_mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.VariancePopulationProportion import var_pop_proportion
from Statistics.Proportion import proportion
from Statistics.SampleVariance import var_sample_proportion
from Statistics.SampleMean import sampleMean
from Statistics.Pvalue import p_value
from Statistics.SampleStandardDeviation import sample_st_dev
from CSVReader.CSVReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        #self.data = CsvReader('Tests/Data/female_data.csv')
        super().__init__()
        pass

    def pop_mean(self, data):
        self.result = population_mean(data)
        return self.result

    def med(self, data):
        self.result = median(data)
        return self.result

    def mod(self, data):
        self.result = mode(data)
        return self.result

    def population_st_dev(self, data):
        self.result = pop_stand_dev(data)
        return self.result

    def variance_pop_proportion(self, data):
        self.result = var_pop_proportion(data)
        return self.result

    def z_score(self, data):
        self.result = z_score(data)
        return self.result

    def confidence_interval(self, data):
        self.result = confidence_interval(data)
        return self.result

    def population_variance(self, data):
        self.result = population_variance(data)
        return self.result

    def pop_correlation_coefficient(self, data):
        self.result = population_variance(data)
        return self.result

    def proportion(self, data):
        self.result = proportion(data)
        return self.result

    def p_value(self, data):
        self.result = p_value(data)
        return self.result

    def sample_mean(self, data):
        self.result = sampleMean(data)
        return self.result

    def sample_st_dev(self, data):
        self.result = sample_st_dev(data)
        return self.result

    def var_sam_prop(self, data):
        self.result = var_sample_proportion(data)
        return self.result
