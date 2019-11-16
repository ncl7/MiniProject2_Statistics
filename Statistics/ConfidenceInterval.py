from Statistics.SampleMean import sampleMean
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Calculators.Division import division
from Calculators.SquareRoot import square_root
from Calculators.Multiplication import multiplication
from Calculators.Subtraction import subtraction
from Calculators.Addition import addition


def confidence_interval(data):
    # For a Confidence Interval of 95%
    z_value = 1.960
    mean = sampleMean(data)
    sd = pop_stand_dev(data)
    x = len(data)
    y = division(square_root(x), sd)
    margin_of_error = multiplication(z_value, y)
    a = subtraction(mean, margin_of_error)
    b = addition(mean, margin_of_error)
    array = []
    c = array[a, b]
    return c

