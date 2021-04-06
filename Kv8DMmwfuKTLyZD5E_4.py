
def make_dartboard(n):
    half = -(-n//2)
    base = list('1' * n)
    a = [int(''.join(base))]
​
    for x in range(1,half):
        base[x:n-x] = str(x+1) * (n - (x*2)) 
        a.append(int(''.join(base)))
​
    return a + a[-2::-1] if n % 2 else a+a[::-1]

