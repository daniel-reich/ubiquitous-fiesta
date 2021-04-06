
def easter_date(y):
    g = y % 19 + 1
    s = (y-1600) // 100 - (y - 1600) // 400
    l = (((y - 1400) // 100) * 8) // 25
    p1 = (3 - 11*g + s - l) % 30
    if (p1 == 29) or (p1 == 28 and g > 11):
        p = p1 - 1
    else:
        p = p1
    d = (y + (y//4) - (y//100) + (y//400)) % 7
    d1 = (8 - d) % 7
    p2 = (3 + p) % 7
    x1 = (5 - d - p) % 7
    x = (4 - d - p) % 8
    e = p + 1 + (4 - d - p) % 7
    if e < 11:
        return 'March '+str(int(e+21))
    else:
        return 'April '+str(int(e-10))

