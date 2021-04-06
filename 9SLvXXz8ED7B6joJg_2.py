
def lets_meet(distance, va, vb):
    t = distance / (va + vb)
    h = int(t)
    m = 60 * (t - h)
    ans = str(h) + "h " + str(int(m)) + "min " + str(int(60 * (m - int(m)))) + "s"
    return ans

