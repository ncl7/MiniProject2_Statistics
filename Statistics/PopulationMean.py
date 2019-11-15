from Calculators.Division import division


def population_mean(data):
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    n = len(new_data)
    return round(division(n, sum(new_data)), 8)
