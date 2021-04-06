
def overlap(s1, s2):
    for i in range(len(s1)):
        if s2.startswith(s1[i:]):
            return s1[:i] + s2
    return s1 + s2

