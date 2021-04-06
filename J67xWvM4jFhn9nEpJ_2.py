
def build_oms(s): # odd magic squares
    if s % 2 == 0:
        s += 1
    q = [[0 for j in range(s)] for i in range(s)]
    p = 1
    i = s // 2
    j = 0
    while p <= (s * s):
        q[i][j] = p
        ti = i + 1
        if ti >= s: ti = 0
        tj = j - 1
        if tj < 0: tj = s - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1
    return q
​
def build_sems(s): # magic square singly even s
    q = [[0 for j in range(s)] for i in range(s)]
    z = s // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = build_oms(z)
    for j in range(0, z):
        for i in range(0, z):
            a = o[i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d
    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, s):
            if i < lc or i > s - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t
    return q
​
def build_dems(n): # doubly even magic squares
    arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 
    for i in range(0,n//4): 
        for j in range(0,n//4): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
    for i in range(0,n//4): 
        for j in range(3 * (n//4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
    for i in range(3 * (n//4),n): 
        for j in range(0,n//4): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
    for i in range(3 * (n//4),n): 
        for j in range(3 * (n//4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
    for i in range(n//4,3 * (n//4)): 
        for j in range(n//4,3 * (n//4)): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
    return arr
​
def make_magic(s):
    if s%2:
        return build_oms(s)
    elif s%4==0:
        return build_dems(s)
    else:
        return build_sems(s)

