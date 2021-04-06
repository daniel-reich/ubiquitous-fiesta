
def sums_up(lst):
    indices = {lst[i]: i for i in range(len(lst))}
    L = []
    for k in lst:
        if k != 4 and 8 - k in indices and indices[k] < indices[8 - k]:
            L.append([min(k, 8 - k), max(k, 8 - k), max(indices[k], indices[8 - k])])
    L.sort(key=lambda x: x[2])
    return {"pairs": [el[:2] for el in L]}

