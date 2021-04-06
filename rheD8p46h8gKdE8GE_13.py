
def grayscale(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            add, s = [], 0
            for k in lst[i][j]:
                k = min(255, k)
                k = max(0, k)
                s += k
            a = round(s / 3)
            add = [a, a, a]
            lst[i][j] = add
    return lst

