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

    def pop_mean(self):
        self.result = population_mean(self.data)
        return self.result

    def med(self):
        self.result = median(self.data)
        return self.result

    def mod(self):
        self.result = mode(self.data)
        return self.result

    def population_st_dev(self):
        self.result = pop_stand_dev(self.data)
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

    def pop_correlation_coefficient(self):
        self.result = population_variance(self.data)
        return self.result

    def proportion(self,):
        self.result = proportion()
        return self.result

    def p_value(self,):
        self.result = p_value()
        return self.result

    def sample_mean(self):
        self.result = sampleMean()
        return self.result

    def sample_st_dev(self):
        self.result = sample_st_dev()
        return self.result

    def var_sam_prop(self):
        self.result = var_sample_proportion()
        return self.result
