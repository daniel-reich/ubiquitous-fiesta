
def bed_time(*times):
    r = []
    for i in times:
        h1, m1 = i[0].split(":")
        h2, m2 = i[1].split(":")
        h = int(h1) - int(h2)
        m = int(m1) - int(m2)
        if h < 0:
            h = 24 + h
        if m < 0:
            m = 60 + m
            h -= 1
        add = "{}:{}".format(str(h).zfill(2), str(m).zfill(2))
        r.append(add)
    return r

