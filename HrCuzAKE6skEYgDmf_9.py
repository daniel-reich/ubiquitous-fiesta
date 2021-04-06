
def pairs(lst):
    l = len(lst)
    m = l // 2
    myans = []
    if l % 2 == 0:
        for i in range(m):
            myans.append([lst[i],lst[l-i-1]])
    else:
        for i in range(m):
            myans.append([lst[i],lst[l-i-1]])
        myans.append([lst[m],lst[m]])
        
    return myans

