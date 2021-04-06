
def min_length(lst, n):
    if max(lst) > n: return 1
    smol = [x for x in range(2, len(lst)+1) for y in range(len(lst)-(x-1)) if sum([lst[y+z] for z in range(x)]) > n]
    return min(smol) if smol else -1

