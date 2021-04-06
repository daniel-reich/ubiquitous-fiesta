
def find_the_difference(s, t):
    s = sorted(s)
    t = sorted(t)
    for i in range(len(s)):
        if t[i] != s[i]:
            return t[i]
    return t[-1]

