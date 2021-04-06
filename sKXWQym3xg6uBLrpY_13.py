
def iqr(lst):
    lst = sorted(lst)
    m = len(lst)//2
    if len(lst) % 2 == 0:
        Q1L = lst[:m]
        Q3L = lst[m:]
        mm = len(Q1L) // 2
        if len(Q1L) % 2 == 0:
            Q1 = (Q1L[mm] + Q1L[mm-1])/2
        else:
            Q1 = Q1L[mm]
        
        if len(Q3L) % 2 == 0:
            Q3 = (Q3L[mm] + Q3L[mm-1])/2
        else:
            Q3 = Q3L[mm]
    else:
        Q1L = lst[:m]
        Q3L = lst[m+1:]
        mm = len(Q1L) // 2
        if len(Q1L) % 2 == 0:
            Q1 = (Q1L[mm] + Q1L[mm-1])/2
        else:
            Q1 = Q1L[mm]
        
        if len(Q3L) % 2 == 0:
            Q3 = (Q3L[mm] + Q3L[mm-1])/2
        else:
            Q3 = Q3L[mm]
    
    return Q3-Q1

