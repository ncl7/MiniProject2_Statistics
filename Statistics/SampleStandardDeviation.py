from Calculators.Subtraction import subtraction
from Calculators.Division import division
from Calculators.SquareRoot import square_root
from Calculators.Squaring import square
from Statistics.SampleMean import sampleMean
from Calculators.Addition import addition


def sample_st_dev(data):

    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    sample_data = new_data[0:999]
    n = len(sample_data)
    x_bar = sampleMean(sample_data)

    for dev in n:

        dev = subtraction(n, x_bar)
        square_x_bar = square(dev)
        add = addition(square_x_bar, square_x_bar)
        divide = division(add, n)
    return round(square_root(divide), 8)

