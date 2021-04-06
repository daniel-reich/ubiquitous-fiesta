
def sieve(n):
    arr = (n+1)*[True]
    arr[0] = False
    arr[1] = False
    for x in range(2,int(n**0.5)+1):
        if arr[x]:
            for y in range(2,n//x+1):
                arr[x*y] = False
    return arr
​
def pArray(n):
    ret = []
    pSieve = sieve(n)
    for x in range(2,n+1):
        if pSieve[x]:
            ret.append(x)
    return ret
​
def factors(n):
    facs = []
    for x in pArray(n):
        if x > n: break
        while n%x == 0:
            facs.append(x)
            n //= x
    if n > 1: facs.append(n)
    return facs
​
​
def prime_factorize(num):
  return factors(num)

