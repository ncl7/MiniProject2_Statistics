from Statistics.PopulationMean import population_mean
from Calculators.Subtraction import subtraction
from Calculators.Squaring import square
from Calculators.Division import division


def population_variance(data):
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    u = population_mean(new_data)
    deviations = subtraction(new_data, u)
    sq_deviations = square(deviations)
    x = len(new_data)
    y = sum(sq_deviations)
    d = division(x, y)
    return d
