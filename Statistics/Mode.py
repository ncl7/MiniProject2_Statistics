def mode(data):
    return round(max(set(data), key=data.count), 1)
