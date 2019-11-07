import math


def sampleSTD(s, i, x, n):
    s = math.sqrt(sum(i - x) * (i - x) / (n - 1))
    return s
