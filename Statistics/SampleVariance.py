from Statistics.sampleData import sampleData
from Statistics.Proportion import proportion
from Calculators.Subtraction import subtraction
from Calculators.Division import division
from Calculators.Multiplication import multiplication



def var_sample_proportion(data, sample_size):
    height = 0
    sample = sampleData(data, sample_size)
    sample_values = len(sample)
    x = proportion(data)
    z = subtraction(1, x)
    y = subtraction(sample_values, 1)
    for height in sample:
        height = multiplication(x, z)
    return division(height, y)