
def bonus(days):
    m = days
    if m < 33:
        return 0
    elif m>32:
        j = days-32
    if j<9:
        jj = 325*j
        return jj
    elif j>8 and j<17:
        jj = 325*8
        mm = j-8
        kk = (mm*550)+jj
        return kk
    elif j>16:
        jj = 325*8
        mm = j-8
        kk = (8*550)+jj
        tt = mm-8
        xx = (tt*600)+kk
        return xx

