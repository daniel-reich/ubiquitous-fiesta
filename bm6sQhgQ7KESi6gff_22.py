
def find_the_difference(s, t):
    t = sorted(list(t))
    s = sorted(list(s))
    for i in range(len(t)-1):
        if s[i]!=t[i]:return t[i]
    return t[-1]

