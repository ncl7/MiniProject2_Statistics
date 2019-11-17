from Calculators.Addition import addition
from Calculators.Division import division


def proportion(data):
    len_new = len(data)
    prop_data = []
    for x in data:
        if x > 64:
            prop_data.append(x)
    len_prop = len(prop_data)
    return len_prop / len_new

