from Calculators.Addition import addition
from Calculators.Division import division


def proportion(data):
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    len_new = len(new_data)
    prop_data = []
    for x in new_data:
        if x > 64:
            prop_data.append(x)
    len_prop = len(prop_data)
    return len_prop / len_new

