from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import subtraction
from Calculators.Calculator import division


def pop_correlation_coefficient(data_x, data_y):
    # x_data = [num for elem in data_x for num in elem]
    # y_data = [num for elem in data_y for num in elem]
    new_x_data = [float(x) for x in data_x]
    new_y_data = [float(x) for x in data_y]
    x = pop_stand_dev(new_x_data)
    y = pop_stand_dev(new_y_data)
    divisor = multiplication(x, y)
    z = len(new_x_data)

    # Covariance calculation:
    a = subtraction(data_x, population_mean(data_x))
    b = subtraction(data_y, population_mean(data_y))
    c = multiplication(a, b)
    covariance = division(z, (sum(c)))

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    return d
