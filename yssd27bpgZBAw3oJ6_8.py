
def probability(u):
    ss = 365**u
    distinctbd = 1
    count = 0
    for days in range(365, 325, -1):
        if count == u:
            break
        distinctbd *= days
        count += 1
    prob = 1 - (distinctbd/ss)
    return round(prob,2)

