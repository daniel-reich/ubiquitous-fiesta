
def lengthen(s1, s2):
    a = max(len(s1), len(s2))
    if len(s1) < len(s2):
        return (s1 * a)[:a]
    else:
        return (s2 * a)[:a]

