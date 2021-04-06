
def max_ham(s1, s2):
    if sorted(s1) == sorted(s2):
        nl = sum(1 for l in range(len(s1)) if s1[l] != s2[l])
    return False if sorted(s1) != sorted(s2) else True if nl == len(s1) else nl

