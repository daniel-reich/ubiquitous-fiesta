
def sliding_sum(lst, n, k):
    lst2 = [lst[i:i+n] for i in range(0, len(lst))]
    return [i for i in lst2 if sum(i) == k and len(i) == n]

