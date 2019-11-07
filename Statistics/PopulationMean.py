from Calculators.Addition import addition
from Calculators.Division import division


def population_mean(data):
    n = len(data)
    total = 0
    for item in data:
        total = addition(total, item)
    return division(total, n)
