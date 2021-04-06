
def prime(n):
    a = 3
    p = [2]
    while len(p) < n:
        isPrime = True
        for i in range(2,int(a**.5)+1):
            if a%i == 0:
                isPrime = False
        if isPrime:
            p.append(a)
        a += 2
    return p
def primorial(n):
    p = prime(n)
    myans = 1
    for i in p:
        myans *= i
    return myans

