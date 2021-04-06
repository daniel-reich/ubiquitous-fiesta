
def probability(u):
    pu = 1
    for i in range(u):
        pu *= 365 - i
    return round(1 - (pu / 365**u), 2)

