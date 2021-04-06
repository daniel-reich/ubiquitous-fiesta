
def lengthen(s1, s2):
    n = len(max(s1, s2, key=len))
    return (n * min(s1, s2, key=len))[:n]

