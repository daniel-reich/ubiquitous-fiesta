
def make_magic_odd(n):
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]
​
    # initialize position of 1
    i = n / 2
    j = n - 1
​
    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:
​
            # next number goes out of
            # right side of square
            if j == n:
                j = 0
​
            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1
​
        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1
​
        j = j + 1
        i = i - 1  # 1st condition
    return magicSquare
​
​
def make_magic_square_doubly_even(n):
    # 2-D matrix with all entries as 0
    arr = [[(n * y) + x + 1 for x in range(n)] for y in range(n)]
​
    # Change value of array elements at fix location
    # as per the rule (n*n+1)-arr[i][[j]
​
    # Corners of order (n/4)*(n/4)
    # Top left corner
    for i in range(0, n // 4):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j]
​
            # Top right corner
    for i in range(0, n // 4):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j]
​
            # Bottom Left corner
    for i in range(3 * (n // 4), n):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j]
​
            # Bottom Right corner
    for i in range(3 * (n // 4), n):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j]
​
            # Centre of matrix,order (n/2)*(n/2)
    for i in range(n // 4, 3 * (n // 4)):
        for j in range(n // 4, 3 * (n // 4)):
            arr[i][j] = (n * n + 1) - arr[i][j]
    return arr
​
​
def make_magic_square_singly_even(n):
    if n % 2 == 1:
        n += 1
    while n % 4 == 0:
        n += 2
​
    q = [[0 for _ in range(n)] for _ in range(n)]
    z = n // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = make_magic_odd(z)
​
    for j in range(0, z):
        for i in range(0, z):
            a = o[i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d
​
    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, n):
            if i < lc or i > n - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t
​
    return q
​
def make_magic(n):
    if n % 2 != 0:
        return make_magic_odd(n)
    elif n % 4 == 0:
        return make_magic_square_doubly_even(n)
    else:
        return  make_magic_square_singly_even(n)

