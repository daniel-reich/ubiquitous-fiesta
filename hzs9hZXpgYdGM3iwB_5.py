
def alternating_caps(txt):
    b = txt.replace(" ","")
    a = list(b)
    for i in range(0,len(a)):
        if i %2==0:
            a[i] = a[i].upper()
        else:
            a[i] = a[i].lower()
    c= ''.join(a)
    d = txt.split()
    result = []
    result.append(c[0:len(d[0])])
    n=m=0
    for k in range(0,len(d)-1):
        n += len(d[k])
        result.append(c[n :n + len(d[k+1])])
    return ' '.join(result)

