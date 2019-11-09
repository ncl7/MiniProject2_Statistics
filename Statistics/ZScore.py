from Statistics.PopulationMean import population_mean
from Statistics.SampleStandardDeviation import sample_st_dev
from Calculators.Subtraction import subtraction
from Calculators.Division import division


def z_score(data):
    x = 64
    u = population_mean(data)
    sample_sd = sample_st_dev(data)
    y = subtraction(x, u)
    return division(sample_sd, y)
