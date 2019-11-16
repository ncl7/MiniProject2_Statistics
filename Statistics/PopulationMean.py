from Calculators.Division import division


def population_mean(data):
    n = len(data)
    return round(division(n, sum(data)), 8)
