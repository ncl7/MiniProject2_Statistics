from Statistics.PopulationMean import population_mean
from Calculators.Calculator import square_root


def pop_stand_dev(data):
    u = population_mean(data)
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    leng = len(new_data)
    return round(square_root(sum([(element - u) ** 2 for element in new_data]) / leng), 3)



