from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import subtraction
from Calculators.Calculator import division


def pop_correlation_coefficient(x_data, y_data):
    st_x = pop_stand_dev(x_data)
    st_y = pop_stand_dev(y_data)
    divisor = multiplication(st_x, st_y)
    x_length = len(x_data)

    # Covariance calculation:
    a = subtraction(x_data, population_mean(x_data))
    b = subtraction(y_data, population_mean(y_data))
    c = multiplication(a, b)
    covariance = division(x_length, (sum(c)))

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    return d
