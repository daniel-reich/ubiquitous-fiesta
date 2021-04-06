
def max_sum_pair(lst):
    total = 0
    size = len(lst)
    for i in range(size):
        for j in range(i, size):
            for k in range(j + 1,size):
                for l in range(k,size):
                    a = sum(lst[i:j + 1])
                    b = sum(lst[k:l + 1])
                    temp = max(a + b, a, b)
                    if temp > total:
                        total = temp
    return total

