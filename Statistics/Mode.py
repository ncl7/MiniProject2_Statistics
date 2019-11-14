def mode(data):
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    return max(set(new_data), key=new_data.count)
