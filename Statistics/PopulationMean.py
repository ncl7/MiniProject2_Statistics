from Calculators.Addition import addition
from Calculators.Division import division


def population_mean(data):
    new_data = [float(x) for x in data]
    n = len(new_data)
    total = 0
    for item in new_data:
        total = addition(total, item)
    return division(total, n)
