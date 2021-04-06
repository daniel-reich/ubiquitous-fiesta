
def mystery_func(n):
    i = 0
    j = 0
    lst = []
    while j < n:
        j = 2**i
        lst.append(j)
        i +=1
    return int(str("2"*(len(lst)-2))+str(n-lst[len(lst)-2]))

