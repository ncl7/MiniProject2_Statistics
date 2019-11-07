from Calculators.PopulationMean import population_mean
from Calculators.Squaring import square


def population_variance(data):
    d = sum((square(data - population_mean)))/len(list)
    return d
