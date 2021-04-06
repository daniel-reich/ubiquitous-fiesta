
def subtract_matrix(lst1, lst2):
    return [[v1 - v2 if type(v1) in [int, float] and type(v2) in [int, float]
             else int(v1) - int(v2) for v1, v2 in zip(r1, r2)]
            for r1, r2 in zip(lst1, lst2)]

