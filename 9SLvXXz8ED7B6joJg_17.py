
def lets_meet(distance, va, vb):
    d = ((va / (va + vb) * distance) / va * 3600)
    m, s = (divmod(d, 60))
    if round(s) == 60:
        m += 1
        s -= 60
    h, m = (divmod(m, 60))
    return str(int(h)) + "h " + str(int(m)) + "min " + str(int(s)) + "s"

