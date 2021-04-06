
import statistics
import math
​
def get_quartiles(lst, method):
    lst = sorted(lst)
    l = len(lst)
    myans = [lst[0],0,statistics.median(lst),0,lst[-1]]
    
    if method == 'T':
        if l%2 == 0:
            a = lst[:l//2]
            b = lst[l//2:]
            myans[1] = statistics.median(a)
            myans[3] = statistics.median(b)
        else:
            a = lst[:l//2+1]
            b = lst[l//2:]
            myans[1] = statistics.median(a)
            myans[3] = statistics.median(b)
    if method == 'MM':
        if l%2 == 0:
            a = lst[:l//2]
            b = lst[l//2:]
            myans[1] = statistics.median(a)
            myans[3] = statistics.median(b)
        else:
            a = lst[:l//2]
            b = lst[l//2+1:]
            myans[1] = statistics.median(a)
            myans[3] = statistics.median(b)
    if method == 'MS':
        nn = (len(lst)+1)/4     
        if nn - math.floor(nn) <.5:
            n = math.floor(nn)
        else:
            n = math.ceil(nn)
        myans[1] = lst[n-1]
        nn = 3*(len(lst)+1)/4
​
        if nn - math.floor(nn) <=.5:
            n = math.floor(nn)
        else:
            n = math.ceil(nn)
        myans[3] = lst[n-1]
    return myans

