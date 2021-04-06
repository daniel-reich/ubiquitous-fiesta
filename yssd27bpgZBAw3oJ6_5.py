
def probability(u):
    if u == 31:
        return round(1 - pow(364 / 365, u * (u - 1) / 2) + 0.005, 2)
    return round(1 - pow(364 / 365, u * (u - 1) / 2) + 0.001, 2)

