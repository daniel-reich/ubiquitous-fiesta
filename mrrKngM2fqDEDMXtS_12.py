
def can_patch(b, p):
    a = []
    gap = 0
    for i in b:
        if i == 1:
            if gap > 1:
                a.append(gap)
            gap = 0 
        elif i == 0:
            gap+=1
    if gap > 1:
        a.append(gap)
    if len(a) > len(p):
        return False
    for i in a:
        if i-1 in p:
            p.remove(i-1)
            gap+=1
        elif i in p:
            p.remove(i)
            gap+=1
    return len(a)==gap

