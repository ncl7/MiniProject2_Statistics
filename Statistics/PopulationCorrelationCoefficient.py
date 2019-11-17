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
        product = int(product)
        # index += 1
        # print(index, product)

    total = []
    for n in range(product):
        total.append(z)
        print(total)

    sum_total = sum(total)

    covariance = division(z, sum_total)

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    print(d)
    return d
