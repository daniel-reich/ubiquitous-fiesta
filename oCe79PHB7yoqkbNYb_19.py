
def break_point(num):
    l = []
    i = 0
    s1 = 0
    s2 = 0
    for a in str(num):
        l.append(a)
    while i < len(l) :
        s1 ,s2 = 0, 0
        for a in l[:i]:
            s1 += int(a)
        for b in l[i:]:
            s2 += int(b)
        i+=1
        if s1 == s2:
            return True
    return False

