from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import division


def pop_correlation_coefficient(data_x, data_y):
    x = pop_stand_dev(data_x)
    y = pop_stand_dev(data_y)
    divisor = multiplication(x, y)
    z = len(data_x)

    # Covariance calculation:
    d = population_mean(data_x)
    e = population_mean(data_y)
    a = [(element - d) for element in data_x]
    b = [(element - e) for element in data_y]
    for index, item in enumerate(a):
        product = a[index] * b[index]
        index += 1
        print(index, product)

    covariance = division(z, product)
    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    print(d)
    return d
