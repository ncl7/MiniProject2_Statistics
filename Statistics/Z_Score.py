from Statistics.PopulationMean import population_mean
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Calculators.Subtraction import subtraction
from Calculators.Division import division


def z_score(data):
    u = population_mean(data)
    # data = [float(num) for elem in range(data) for num in elem]
    new_data = [float(x) for x in data]
    x = new_data[1]
    # X Value: 0.5641974007
    pop_sd = pop_stand_dev(new_data)
    y = subtraction(x, u)
    return division(pop_sd, y)
