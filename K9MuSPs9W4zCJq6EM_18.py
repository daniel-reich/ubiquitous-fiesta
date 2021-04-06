
def cycle_length(lst,n):
    from copy import deepcopy
    newList = sorted(lst)    
    
    count = 0    
    current = n   
​
    print(newList)
    print(newList.index(current))    
    print(lst)
    
    while lst.index(current) != newList.index(current):
        oldList = deepcopy(lst)
        
        sub = lst[newList.index(current)]
        lst[newList.index(current)] = current
        lst[lst.index(current)] = sub
        current = sub
        
        if oldList != lst:
            count += 1
    
    print(count)
    return count

