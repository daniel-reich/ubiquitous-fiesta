
def gcd(n, d):
    while d:
        n, d = d, n%d
    return n
​
def sim_prop_frac(n):
  return len({(a//gcd(a, b), b//gcd(a, b)) for a in range(1, n+1) for b in range(1, n+1) if a < b})

