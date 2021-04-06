
def probability(u):
    x = 1
    for i in range(u):
        x *= (365 - i) / 365
    return round(1 - x, 2)

