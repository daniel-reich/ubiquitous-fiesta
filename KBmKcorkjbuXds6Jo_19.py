
def chocolates_parcel(n_small, n_big, order):
    dp1 = 0
    dp2 = 0
    nbu = 0
    nsu = 0
    while (dp2 <= (order - 5)) and (nbu < n_big):
        dp1 = dp2
        dp2 += 5
        nbu += 1
    fdp = dp2
    while (fdp < order) and (nsu <= n_small):
        fdp += 2
        nsu += 1
​
    if not fdp == order:
        fdp = dp1
        nsu = 0
        while (fdp < order) and (nsu <= n_small):
            fdp += 2
            nsu += 1
​
        if not fdp == order:
            return -1
    return nsu

