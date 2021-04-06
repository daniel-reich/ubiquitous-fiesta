
from math import ceil
​
def get_median(lst):
    n = len(lst)
    return lst[n//2] if n%2 else (lst[n//2 - 1] + lst[n//2])/2
​
def get_quartiles(lst, method):
    lst.sort()
    n = len(lst)
​
    if method == 'MS':
        v1, v3 = (n+1)/4, 3*(n+1)/4
        q1 = lst[ceil(v1) - 1] if str(v1).endswith('.5') else lst[round(v1) - 1]
        q3 = lst[int(v3) - 1] if str(v3).endswith('.5') else lst[round(v3) - 1]
    elif n%2 == 0:
        q1 = get_median(lst[:n//2])
        q3 = get_median(lst[n//2:])
    else:
        if method == 'T':
            q1 = get_median(lst[:n//2+1])
            q3 = get_median(lst[n//2:])
        else:
            q1 = get_median(lst[:n//2])
            q3 = get_median(lst[n//2+1:])            
    
    return [lst[0], q1, get_median(lst), q3, lst[-1]]

