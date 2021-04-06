
def nearest_chapter(c, p):
    lst = [c[i] for i in c]; dif = [abs(i-p) for i in lst]; res = min(dif)
    return sorted(([[i for i in c][ele] for ele, i in enumerate(dif) if i == res]))[-1]

