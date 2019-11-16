from Statistics.Proportion import proportion
from Calculators.Subtraction import subtraction
from Calculators.Division import division
from Calculators.Multiplication import multiplication


def var_pop_proportion(data):
    p = proportion(data)
    q = subtraction(1, p)
    n = len(data)
    return division(n, multiplication(p, q))
