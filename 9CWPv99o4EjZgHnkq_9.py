
def divide(lst, n):
    lst.append(99)
    lst.append(99)
    myans = []
    a = 0
    while len(lst) > 2:
        for b in range(1,len(lst)):
            if sum(lst[a:b]) > n:
                myans.append(lst[a:b-1])
                del lst[a:b-1]
                break
​
    return myans

