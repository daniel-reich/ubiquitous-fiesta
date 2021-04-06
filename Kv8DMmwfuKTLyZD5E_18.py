
def make_dartboard(n):
​
    a, b, c, d = [], [], [], []
    
    if n == 1:
        return [1]
    
    if n%2 == 0:
        for i in range(1,n//2+2):
            a.append([])
            b.append([])
            for j in range(1,i):
                a[i-2].append(str(j))
        a, b = a[:-1], b[:-1]  
        for k in range(len(a)):
            for i in range(n - 2*len(a[k]) ):
                b[k].append(a[k][-1])
            b[k] = a[k] + b[k] + a[k][::-1]
        c = (b + b[::-1])
​
    if n%2 !=0:
        for i in range(1,n//2+3):
            a.append([])
            b.append([])
            for j in range(1,i):
                a[i-2].append(str(j))
        a, b = a[:-1], b[:-1]  
        for k in range(n//2):
            for i in range(n - 2*len(a[k]) ):
                b[k].append(a[k][-1])
            b[k] = a[k] + b[k] + a[k][::-1]
        b[-1]=a[-1]+a[-2][::-1]
        c = (b + b[::-1][1:])
    for i in c:
        d.append(int("".join(i))) 
    return (d)

