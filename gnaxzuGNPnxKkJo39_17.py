
def easter_date(y):
    g = y % 19 + 1
    s = (y - 1600) // 100 - (y - 1600) // 400
    l = (((y - 1400) // 100) * 8) // 25
    pp = (3 - 11 * g + s - l) % 30
    if pp == 29 or (pp == 28 and g > 11):
        p = pp - 1
    else:
        p = pp
    d = (y + y // 4 - (y // 100) + (y // 400)) % 7
    dp = (8 - d) % 7
    ppp = (80 + p) % 7
    xp = (5 - d - p) % 7
    x = (4 - d - p) % 7 + 1
    e = p + x
    if e < 11:
        return "March " + str(e + 21)
    else:
        return "April " + str(e - 10)

