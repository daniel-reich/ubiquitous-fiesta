
def goldbach_conjecture(n):
    if n > 2 and n % 2 == 1:
        return []
    if n <= 2:
        return []
​
    p = []
​
    for i in range(2,n):
        isPrime = True
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            p.append(i)
​
    for i in range(len(p)-1,-1,-1):
        if n - p[i] in p:
            return [n-p[i],p[i]]

