
def primes(n):
    era = [True] * n
    era[:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if era[i]:
            era[i*i::i] = [False] * ((n-1)//i-i+1)
    return [i for i, b in enumerate(era) if b]
​
def semiprimes(n):
    res1, res2 = [], []
    pr = primes(n//2 + 1)
    print(pr)
    for i, a in enumerate(pr):
        if a * a < n:
            res1.append(a * a)
        for b in pr[i+1:]:  # itertools.islice is better here
            if a * b >= n:
                break
            res1.append(a * b)
            res2.append(a * b)
    return sorted(res1), sorted(res2)

