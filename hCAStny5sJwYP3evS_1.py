
def is_early_bird(_range, n):
    a,z,q='',[],0
    for x in range(_range+1):
        a+=str(x)
    count = start = 0
    while True:
        start = a.find(str(n), start) + 1
        if start > 0:
            count+=1
        else:
            break
    for x in range(count):
        m=[]
        for y in range(len(str(n))):
            if not m:
                m.append(a.index(str(n),q+1))
                q=a.index(str(n),q+1)
            else:
                m.append(m[-1]+1)
        z.append(m)
    if count>1:
        z.append("Early Bird!")
    return(z)

