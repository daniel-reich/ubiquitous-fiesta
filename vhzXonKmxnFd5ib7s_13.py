
def matrix_multiply(a, b):
    r1 = len(a)
    c1 = len(a[0])
    r2 = len(b)
    c2 = len(b[0])
​
    if c1 != r2:
        return 'invalid'
​
    c = []
    for i in range(len(a)):
        temp=[]
        for j in range(len(b[0])):
            s = 0
            for k in range(len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)
    
    return c

