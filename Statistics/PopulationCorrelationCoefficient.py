from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import subtraction
from Calculators.Calculator import division


def pop_correlation_coefficient(data_x, data_y):
    # x_data = [num for elem in range(data_x) for num in elem]
    # y_data = [num for elem in range(data_y) for num in elem]
    # new_x_data = [range(x) for x in data_x]
    # new_y_data = [range(x) for x in data_y]
    new_x_data = data_x
    new_y_data = data_y
    x = pop_stand_dev(new_x_data)
    y = pop_stand_dev(new_y_data)
    divisor = multiplication(x, y)
    z = len(new_x_data)

    # Covariance calculation:
    d = population_mean(new_x_data)
    e = population_mean(new_y_data)
    a = [(element - d) for element in new_x_data]
    b = [(element - e) for element in new_y_data]
    for index, item in enumerate(a):
        product = a[index] * b[index]
        index += 1
        print(index, product)

    covariance = division(z, product)
    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    print(d)
    return d
