
def is_pandigital(n):
    a=[]
    b=[]
    for i in str(n):
        if i not in a:
            a.append(int(i))
    for i in range(0,10):
        if i not in a:
            b.append(i)
    if len(b)>=1:
        return False
    else:
        return True

