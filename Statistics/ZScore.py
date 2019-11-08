from Statistics.PopulationMean import population_mean
from Statistics.SampleStandardDeviation import sampleSTD
from Calculators.Division import division
from Calculators.Subtraction import subtraction


def z_score(data):
    u = population_mean(data)
    x = len(data)
    y = subtraction(x, u)
    sample_sd = sampleSTD(data)
    z = division(sample_sd, y)
    return z
