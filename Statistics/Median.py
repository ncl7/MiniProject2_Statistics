from Calculators.Calculator import addition, division


def median(data):
    #data = [num for elem in data for num in elem]
    #new_data = [float(x) for x in data]
    new_data = sorted(data)
    length = len(new_data)
    if length < 1:
        return None
    if length % 2 == 0:
        return division(2.0, addition(new_data[(length - 1) // 2], new_data[(length + 1) // 2]))
    else:
        return new_data[(length - 1) // 2]
