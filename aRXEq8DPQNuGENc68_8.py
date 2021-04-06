
def salt(t):
    s = 10
    for mili_sec in range(1, t * 60000 + 1):
        s = s * 599999 / 600000 + 1 / 600000
    return round(s, 3)

