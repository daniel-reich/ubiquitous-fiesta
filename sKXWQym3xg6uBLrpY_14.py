
def median(lst):
    l = 0
    r = len(lst) - 1
    while r-l >1:
        l += 1
        r -= 1
    if l == r:
        return lst[l]
    else:
        return (lst[l] + lst[r])/2
    
def iqr(lst):
    lst = sorted(lst)
    if not len(lst) % 2:
        q2 = median(lst[len(lst)//2:])
    else:
        q2 = median(lst[len(lst)//2 + 1:])
    q1 = median(lst[:len(lst)//2])    
    return q2 - q1

