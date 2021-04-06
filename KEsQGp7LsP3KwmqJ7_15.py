
def check(lst):    
    for i in range(1,len(lst)):        
        if sorted(lst) == lst[i:] + lst[:i]:
            return 'YES'
    return 'NO'

