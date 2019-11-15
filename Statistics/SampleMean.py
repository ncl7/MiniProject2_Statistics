from Calculators.Addition import addition
from Calculators.Division import division
from Statistics.sampleData import sampleData


def sampleMean(data, sample_size):
    total = 0
    sample = sampleData(data, sample_size)
    sample_values = len(sample)
    for value in sample:
        total = addition(total, value)
    return division(total, sample_values)