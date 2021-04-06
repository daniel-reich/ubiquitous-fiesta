
def sums_up(lst):
    final = []
    [final.append(i) for i in [sorted(i[0]) for i in reversed([[[i, j] for j in lst if i + j == 8 and i != j] for i in lst]) if i] if i not in final]
    return {"pairs": list(reversed(final))}

