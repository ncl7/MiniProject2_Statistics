from Statistics.PopulationMean import population_mean
from Statistics.SampleStandardDeviation import sample_st_dev
from Calculators.Subtraction import subtraction
from Calculators.Division import division


def z_score(data):
    u = population_mean(data)
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    x = new_data[1]
    sample_sd = sample_st_dev(new_data, 1000)
    y = subtraction(x, u)
    return division(sample_sd, y)
