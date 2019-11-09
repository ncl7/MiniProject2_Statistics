from CSVReader.CSVReader import CsvReader
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.SampleMean import sampleMean
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
    a = subtraction(data, sampleMean)
    b = subtraction(data, population_mean)
    c = multiplication(a, b)
    covariance = division(z, (sum(c)))

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    return d
