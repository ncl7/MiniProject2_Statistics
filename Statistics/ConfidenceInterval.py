from Statistics.SampleMean import sampleMean
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Calculators.Division import division
from Calculators.SquareRoot import square_root
from Calculators.Multiplication import multiplication
from Calculators.Subtraction import subtraction
from Calculators.Addition import addition


def confidence_interval(data):
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    # For a Confidence Interval of 95%
    z_value = 1.960
    mean = sampleMean(new_data)
    sd = pop_stand_dev(new_data)
    x = len(new_data)
    y = division(square_root(x), sd)
    margin_of_error = multiplication(z_value, y)
    a = subtraction(mean, margin_of_error)
    b = addition(mean, margin_of_error)
    return a, b

