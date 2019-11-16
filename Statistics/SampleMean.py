from Calculators.Division import division


def sampleMean(data):
    sample_data = data[0:999]
    n = len(sample_data)
    return round(division(n, sum(sample_data)), 1)
