from Statistics.SampleMean import sampleMean
from Calculators.Addition import addition


def sample_st_dev(data):
    mean = sampleMean(data)
    sample_data = data[0:999]
    tot = 0.0
    for x in sample_data:
        tot = addition(tot, (x - mean)**2)
    return round((tot/(len(sample_data) - 1))**0.5, 2)




