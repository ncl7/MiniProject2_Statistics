from Statistics.PopulationMean import population_mean
from Calculators.Subtraction import subtraction
from Calculators.Squaring import square
from Calculators.Division import division


def population_variance(data):
    u = population_mean(data)
    deviations = subtraction(data, u)
    sq_deviations = square(deviations)
    x = len(data)
    y = sum(sq_deviations)
    d = division(x, y)
    return d
