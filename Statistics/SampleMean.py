from Calculators.Division import division


def sampleMean(data):
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    sample_data = new_data[0:999]
    n = len(sample_data)
    return round(division(n, sum(sample_data)), 1)
