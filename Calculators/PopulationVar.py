from Calculators.PopulationMean import population_mean
from Calculators.Calculator import add


def population_variance(data):
    d = square((add(data - population_mean)))/5000
    return d
