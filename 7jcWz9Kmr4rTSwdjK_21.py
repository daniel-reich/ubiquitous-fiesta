
def prime(n):
    l = []
    for i in range(n+1):
        for j in range(n+1):
            if i*j == n:
                l.append(i)
​
    return len(l)
​
def prime_factorize(num):
    l = []
    l2 = []
    for i in range(2,num+1):
        for j in range(num+1):
            if i*j == num:
                l.append(i)
    l.sort()
    for i in l:
        if prime(i) ==2:
            h = 1
            for x in range(num):
                h = h*i
                if h in l:
                 l2.append(i)
​
    return l2
print( prime_factorize(2532))

