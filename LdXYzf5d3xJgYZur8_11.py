
def longest_time(h, m, s):
    h = [h * 60 * 60, h]
    m = [60 * m, m]
    s = [s, s]
    return sorted([h, m, s], key=lambda x : x[0])[-1][-1]

