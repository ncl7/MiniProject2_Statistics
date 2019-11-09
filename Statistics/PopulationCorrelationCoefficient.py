from Statistics.SampleStandardDeviation import sample_st_dev
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.SampleMean import sampleMean
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import subtraction
from Calculators.Calculator import division


def pop_correlation_coefficient(data):
    # x = independent variable ("female_height_sample" sample data)
    # y = dependent variable ("female_height" population data)
    x = sample_st_dev(data)
    y = pop_stand_dev(data)
    divisor = multiplication(x, y)
    z = len(data)

    # Covariance calculation:
    a = subtraction(data, sampleMean)
    b = subtraction(data, population_mean)
    c = multiplication(a, b)
    covariance = division(z, (sum(c)))

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    return d
