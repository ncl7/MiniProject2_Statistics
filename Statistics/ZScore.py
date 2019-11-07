from Statistics.PopulationMean import population_mean
from Statistics.SampleStandardDeviation import sampleSTD
from Calculators.Division import division


def z_score(data):
    u = population_mean(data)
    sam_std = sampleSTD(data)
    return division((len(data) - u), sam_std)
