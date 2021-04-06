
def is_orthogonal(lst1, lst2):
    final = []
    for x in range(len(lst1)):
        dot = (lst1[x] * lst2[x])
        final.append(dot)
        if sum(final) == 0:
            return True
    return False

