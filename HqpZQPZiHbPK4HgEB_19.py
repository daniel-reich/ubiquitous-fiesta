
def maxmin(n):
    def my_min(lst, index):
        mi = 9
        if index == 0:
            for x in lst:
                if 0 < x < mi:
                    mi = x
        else:
            for x in lst:
                if 0 <= x < mi:
                    mi = x
        return mi
    n_max = [int(x) for x in str(n)]
    n_min = n_max.copy()
    n = list(reversed(n_max))
    for x in range(len(n)-1):
        if max(n_max[x+1:]) > n_max[x]:
            i = n_max[x]
            n_max[x] = max(n_max[x+1:])
            n_max[-1*n.index(max(n_max[x+1:]))-1] = i
            break
    for x in range(len(n)-1):
        if 0 <= my_min(n_min[x+1:], x) < n_min[x]:
            i = n_min[x]
            n_min[x] = my_min(n_min[x+1:], x)
            n_min[-1*n.index(my_min(n_min[x+1:], x))-1] = i
            break
    return (int(''.join([str(x) for x in n_max])), int(''.join([str(x) for x in n_min])))

