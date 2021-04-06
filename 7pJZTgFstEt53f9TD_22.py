
def transpose_matrix(lst):
    l = []
    for i in zip(*lst):
        l.append(list(i))
    return l

