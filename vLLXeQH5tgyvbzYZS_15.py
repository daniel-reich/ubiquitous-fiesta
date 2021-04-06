
def is_prim_pyth_triple(lst):
    srt = list(sorted([i**2 for i in lst]))
    if srt[0] + srt[1] != srt[2]:
         return False
    lst2 = []
    for num in lst:
        a = primes(num)
        lst2 += a
    return len(set(lst2)) == len(lst2)
​
def primes(n):
    lst,lst2 = [i for i in range(2,n) if n % i == 0],[]
    for i in lst:
        if isprime(i):
            lst2.append(i)
    return lst2
​
def isprime(n):
    z = 2
    while z < n:
        if n % z == 0:
            return False
        z += 1
    return True

