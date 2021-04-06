
def sliding_sum(lst, n, k):
    result = []
    for i in range(0, len(lst)):
        slice = lst[i:i+n]
        if len(slice) < n:
            slice.append(0)
        if sum(slice) == k:
            result.append(slice)
    return result

