
def eratosthenes(num):
    lst = []
    l = []
​
    for n in range(1,num):
        if n < 2:
            l.append(n)
        for i in range(2, n):
            if n % i == 0:
                l.append(n)
​
    for b in range(1,num):
        if b not in set(l):
            lst.append(b)
    return lst

