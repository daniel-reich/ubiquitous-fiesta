
def rolls(lst):
    s = lst[0]
    for i in range(1,len(lst)):
        if lst[i-1]==6:s+=lst[i]*2
        elif lst[i-1]==1:s+=0
        else: s+=lst[i]
    return  s

