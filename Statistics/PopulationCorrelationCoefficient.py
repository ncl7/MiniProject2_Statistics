from CSVReader.CSVReader import CsvReader
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import subtraction
from Calculators.Calculator import division


def pop_correlation_coefficient(data):
    x_data = CsvReader('Tests/Data/female_height.csv').data
    y_data = CsvReader('Tests/Data/male_height.csv').data
    x = pop_stand_dev(x_data)
    y = pop_stand_dev(y_data)
    divisor = multiplication(x, y)
    z = len(data)

    # Covariance calculation:
    a = subtraction(x_data, population_mean(x_data))
    b = subtraction(y_data, population_mean(y_data))
    c = multiplication(a, b)
    covariance = division(z, (sum(c)))

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    return d
