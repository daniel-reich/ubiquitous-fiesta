
def is_unfair_hurdle(hurdles):
    if len(hurdles) > 3:
        return True
    L = [list(i) for i in zip(*hurdles)]
    ind = [k for k in range(len(L)) if '#' in L[k]]
    return min([ind[i] - ind[i-1] for i in range(1, len(ind))]) < 4

