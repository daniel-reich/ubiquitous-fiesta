
def calc(lst, i, k) :
    c = 0
    res = []
    for j in range(i, len(lst)):
        if lst[j] == 1:
            c += 1
        elif k > 0:
            c += 1
            k -= 1
            res.append(j) 
        elif k == 0:
            return c, res
    return c, res
    
def zero_indices(lst, k):
    maxi = 0
    for i in range(len(lst)) :
        c, tmp = calc(lst, i, k)
        print(i, c, tmp) 
        if c > maxi :
            maxi = c
            res = [h for h in tmp]
    return res

