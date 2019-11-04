from Calculators.PopulationMean import population_mean


def zscore(a, b, c):
    a = 500 # change to actual population number
    b = population_mean
    c = 0.5 # replace with standard deviation method
    d = (a - b) / c
    return d