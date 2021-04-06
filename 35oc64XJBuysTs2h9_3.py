
import math
def get_quartiles(lst, method):
    lst.sort()
    l = len(lst)
    if method == 'T' or 'MM':
        q1 = median(lst[:l//2+1]) if l%2 and method == 'T' else median(lst[:l//2])
        q3 = median(lst[l//2+1:]) if l%2 and method == 'MM' else median(lst[l//2:])
    if method == 'MS':
        i = (l+1)/4
        n1 = round(i) if (l-1) % 4 else math.ceil(i)
        n3 = round(3*i) if (l-1) % 4 else math.floor(3*i)
        q1, q3 = lst[n1-1], lst[n3-1]
    return [lst[0],q1, median(lst), q3, lst[-1]]
​
​
def median(lst):
    l = len(lst)
    return lst[l//2] if l%2 else sum(lst[l//2-1: l//2+1])/2

