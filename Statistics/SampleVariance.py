from Statistics.Proportion import proportion
from Calculators.Subtraction import subtraction
from Calculators.Division import division
from Calculators.Multiplication import multiplication
from Statistics.SampleMean import sampleMean


def var_sample_proportion(data):
    sample = sampleMean(data)
    sample_values = len(sample)
    x = proportion(data)
    z = subtraction(1, x)
    y = subtraction(sample_values, 1)
    for height_el in sample:
        height = multiplication(x, z)
    return division(height, y)
