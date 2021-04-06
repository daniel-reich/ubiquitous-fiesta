
def min_length(lst, n):
    lengths = [j - i for i in range(len(lst))
               for j in range(i + 1, len(lst) + 1) if sum(lst[i: j]) > n]
    return min(lengths) if lengths else -1

