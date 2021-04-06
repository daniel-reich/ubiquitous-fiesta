
def overlap(s1, s2):
    overlap = s2
    while s1.endswith(overlap) == False:
        overlap = overlap[:-1]
    return s1 + s2[len(overlap):]

