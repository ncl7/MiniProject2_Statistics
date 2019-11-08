from Statistics.SampleStandardDeviation import sampleSTD
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.SampleMean import sampleMean
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import subtraction
from Calculators.Calculator import division
# x = independent variable (set as sample for now)
# y = dependent variable (set as population for now)


def pop_correlation_coefficient(data):
    x = sampleSTD(data)
    y = pop_stand_dev(data)
    divisor = multiplication(x, y)
    z = len(data)

    # Covariance calculation format follows:
    # Need sample data CSV
    a = subtraction(sample_data, sampleMean)
    b = subtraction(data, population_mean)
    c = multiplication(a, b)
    covariance = division(z, (sum(c)))
    d = division(divisor, covariance)
    return d
