
def calc_bundled_temp(n, temp):
    t = int(temp[:-2])
    for _ in range(n):
        t *= 1.1
    return '{:.1f}*C'.format(t)

