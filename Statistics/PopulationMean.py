from Calculators.Division import division


def population_mean(data):
    n = len(data)
    sum_total = sum(data)
    return round(division(n, sum_total), 8)
