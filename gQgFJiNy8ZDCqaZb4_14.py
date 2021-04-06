
def overlap(s1, s2):
    if s1 == s2:
        return s1
    s1l = [s1[i : ] for i in range(len(s1))]
    s2l = [s2[ : i] for i in range(1, len(s2) + 1)]
    x = list(set(s1l).intersection(set(s2l)))
    if x == []:
        return s1 + s2
    else:
        return s1 + s2[len(max(x)) : ]

