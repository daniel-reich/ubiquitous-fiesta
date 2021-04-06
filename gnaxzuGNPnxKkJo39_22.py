
def easter_date(y):
    g = y % 19 + 1
    s = (y - 1600) // 100 - (y - 1600) // 400
    l_ = (((y - 1400) // 100) * 8) // 25
    p_ = (3 - 11 * g + s - l_) % 30
    if (p_ == 29) or (p_ == 28 and g > 11):
        p = p_ - 1
    else:
        p = p_
    d = (y + (y // 4) - (y // 100) + (y // 400)) % 7
    e = p + 1 + (4 - d - p) % 7
    if e < 11:
        return 'March {}'.format(21 + e)
    else:
        return 'April {}'.format(e - 10)

