
def farey(n):
    val = []
    l = ['0/1']
    for i in range(1, n+1):
        for j in range(0, n):
            if str(i)+'/'+str(n-j) not in l and i < n-j and i/(n-j) not in val:
                l.append(str(i)+'/'+str(n-j))
                val.append(i/(n-j))
    l2 = l+['1/1']
    return sorted(l2, key=lambda i: eval(i))

