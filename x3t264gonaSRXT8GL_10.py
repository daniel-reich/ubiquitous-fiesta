
def repeating_cycle(n):
    lst = []
    div, r = divmod(1,n)
    
    while r != 0:
        div, r = divmod(r*10, n)
        if [div, r] in lst:
            if lst.index([div, r]) != 0:
                return -1
            return len(lst)
        lst.append([div, r])
    
    return -1

