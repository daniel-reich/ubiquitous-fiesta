
def sliding_sum(lst, n, k):
    new = []
    final = []
    for i in range(len(lst)):
        new.append(lst[i:i+n])
    for j in new:
        if sum(j) == k:
            final.append(j)
    return final

