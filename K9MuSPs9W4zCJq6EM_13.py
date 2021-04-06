
def cycle_length(lst, n):
    
    
    if lst.index(n)  == sorted(lst).index(n):
        return 0
    a = lst.index(n)
    b = sorted(lst).index(n)
        
    result=0
    for i in range(len(lst)):
        n= lst[a]
​
        pos1, pos2 = lst.index(n) , sorted(lst).index(n)
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
        result += 1
        
        if lst[a]  == sorted(lst)[a]:
            break
            
    return (result)

