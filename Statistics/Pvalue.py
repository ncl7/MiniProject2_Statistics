from Statistics.Z_Score import z_score


def p_value(data):
    score = z_score(data)
    value = [float(x) for x in data]
    if value == score[0]:
        return value
    print(value)
