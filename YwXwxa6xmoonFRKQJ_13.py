
def josephus(n):
    if n < 1:
        return False
    a = [1] * n
    i = 0
    killed = 0
    while killed < n-1:
        while a[i] == 0:
            i = (i + 1) % n
        # a[i] = '@'
        # print(a,a)
        # a[i] = 1
        i = (i + 1) % n
        while a[i] == 0:
            i = (i + 1) % n
        # a[i] = 'x'
        # print(a,a)
        # a[i] = 0
        killed += 1
        # print(a,a)
    return a.index(1)
​
​
def josephus(n):
    if n < 1:
        return False
    a = [1] * n
    i = 0
    killed = 0
    while killed < n-1:
        while a[i] == 0:
            i = (i + 1) % n
        # a[i] = '@'
        # print(a,a)
        # a[i] = 1
        i = (i + 1) % n
        while a[i] == 0:
            i = (i + 1) % n
        # a[i] = 'x'
        # print(a,a)
        a[i] = 0
        killed += 1
        # print(a,a)
    return a.index(1)

