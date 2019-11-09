from Statistics.PopulationMean import population_mean
from Statistics.SampleStandardDeviation import sample_st_dev
from Calculators.Division import division


def z_score(data):
    u = population_mean(data)
    sam_std = sample_st_dev(data)
    return division((len(data) - u), sam_std)
