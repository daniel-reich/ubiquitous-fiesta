
def min_swaps(string):
    L = len(string)
    pattern1 = '01' * (L // 2 + 1)
    pattern2 = '10' * (L // 2 + 1)
    return min(sum([string[i] != pattern1[i] for i in range(L)]),
               sum([string[i] != pattern2[i] for i in range(L)]))

