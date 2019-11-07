from Statistics.PopulationMean import population_mean
from Statistics.SampleStandardDeviation import sampleSTD


def z_score(data):
    u = population_mean(data)
    sam_std = sampleSTD(data)
    return (len(data) - u) / sam_std
