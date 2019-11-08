from Statistics.PopulationMean import population_mean
from Calculators.Subtraction import subtraction
from Statistics.SampleStandardDeviation import sampleSTD
from Calculators.Division import division


def z_score(data):
    u = population_mean(data)
    x = len(data)
    y = subtraction(x, u)
    sample_sd = sampleSTD(data)
    z = division(sample_sd, y)
    return z
