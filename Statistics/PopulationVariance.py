from Statistics.PopulationMean import population_mean
from Calculators.Division import division


def population_variance(data):
    u = population_mean(data)
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    leng = len(new_data)
    return round(division(leng, sum([(element - u) ** 2 for element in new_data])), 3)

