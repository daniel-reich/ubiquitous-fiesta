
def probability(u):
    p_no_share = 1.
    for k in range(u):
        p_no_share *= (365 - k) / 365.
    return round(1. - p_no_share, 2)

