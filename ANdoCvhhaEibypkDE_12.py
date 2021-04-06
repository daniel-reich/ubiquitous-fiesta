
def closing_in_sum(n):
    t = str(n)
    l = len(t)
    l2 = l // 2
    myans = 0
    if l % 2 == 0:
        for i in range(l2):
            myans += int(t[i]+t[-(i+1)])
    else:
        for i in range(l2):
            myans += int(t[i]+t[-(i+1)])
        myans += int(t[i+1])
    return myans

