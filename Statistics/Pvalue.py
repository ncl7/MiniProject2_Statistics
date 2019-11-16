from Statistics.Z_Score import z_score


def p_value(data):
    # data = [data]
    n = len(data)
    score = z_score(data)
    for index in range(n):
        if n == score:
            data.append(index)
    return index
