from Statistics.PopulationMean import population_mean
from Calculators.SquareRoot import square_root


def pop_stand_dev(data):
    n = len(data)
    u = population_mean(data)
    return square_root(sum([(element - u) ** 2 for element in data]) / (len(data) - 1))



