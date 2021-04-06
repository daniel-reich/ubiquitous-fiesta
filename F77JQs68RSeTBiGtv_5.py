
def diamond_sum(n):
    s = int((n / 2) + 0.5)
    r = []
    for i in range(s):
        s1 = s + (n * i) + i
        s2 = s + (n * i) - i
        r += [s1] + [s2]
        r += [(n ** 2) + 1 - s1] + [(n ** 2) + 1 - s2]
    return sum(list(set(r)))

