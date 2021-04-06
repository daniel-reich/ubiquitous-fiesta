
def is_rectangle(l):
    if 4 > len(l) < 4:
        return False
    r = []
    for i in l:
        r += [int(i.split(",")[0][1:]), int(i.split(",")[1][:-1])]
    if (r[7] - r[1])**2 + (r[6] - r[0])**2 == (r[5] - r[3])**2 + (r[4] - r[2])**2:
        return True
    return False

