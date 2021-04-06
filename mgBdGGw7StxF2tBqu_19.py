
def duplicates(str1) : 
    l = len(str1)
    x1 = 0 
    l1 = []
    for i in range(l) : 
        x = str1.count(str1[i])
        if (x > 1) and ( str1[i] not in l1) :
            x1 += x-1
            l1.append(str1[i]) 
    return x1

