from Statistics.ZScore import z_score


def p_value(data):
    data = []
    n = len(data)
    score = z_score(data)
    for index in n:
        if n == score:
            data.append(index)
    return index
