
def max_product(lst):
    a = -99999
    for i in range(len(lst)-2):
        for j in range(i+1,len(lst)-1):
            for k in range(j+1,len(lst)):
                a = max(a,lst[i]*lst[j]*lst[k])
    return a 
        
def min_product(lst):
    a = 99999
    for i in range(len(lst)-2):
        for j in range(i+1,len(lst)-1):
            for k in range(j+1,len(lst)):
                a = min(a,lst[i]*lst[j]*lst[k])
    return a

