from Statistics.SampleMean import sampleMean
from Statistics.Proportion import proportion
from Calculators.Subtraction import subtraction
from Calculators.Division import division
from Calculators.Multiplication import multiplication


def var_sample_proportion(data):
    sample_data = data[0:999]
    samp_prop_data = []
    for x in sample_data:
        if x > 64:
            samp_prop_data.append(x)
    samp_len = len(samp_prop_data)
    samp_len_data = len(sample_data)
    p = round(samp_len / samp_len_data, 6)
    q = subtraction(1, p)
    return round(multiplication(p, q) / (samp_len_data - 1), 6)
