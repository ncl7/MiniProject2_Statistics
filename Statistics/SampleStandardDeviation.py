from Calculators.Subtraction import subtraction
from Calculators.Division import division
from Statistics.sampleData import getSample
from Calculators.SquareRoot import square_root
from Calculators.Squaring import square
from Statistics.SampleMean import sampleMean
from Calculators.Addition import addition


def sample_st_dev(data, sample_size):
    dev = 0
    sample = sampleData(data, sample_size)
    sample_values = len(sample)
    x_bar = sampleMean()
    x = sample_values
    n = subtraction(sample_values, 1)
    for dev in sample:
        dev = subtraction(x, x_bar)
        square_x_bar = square(dev)
        add = addition(square_x_bar, square_x_bar)
        divide = division(add, n)
    return square_root(divide)
