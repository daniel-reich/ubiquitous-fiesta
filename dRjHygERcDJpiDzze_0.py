
def lengthen(s1, s2):
    n = max(len(s1),len(s2))
    return ((s1 if len(s1) < len(s2) else s2)*n)[:n]

