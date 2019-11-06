def mode(data):
    c = max(set(data), key=data.count)
    return c
