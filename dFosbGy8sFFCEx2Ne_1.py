
def rank(lst):
    R=[0 for i in range(len(lst))]
    for i in range(len(lst)):
        (r,s)=(1,1)
        for j in range(len(lst)): 
            if j != i and lst[j] < lst[i]: 
                r += 1
            if j != i and lst[j] == lst[i]: 
                s += 1  
        R[i] = (r + (s - 1) / 2)-1
    return R

