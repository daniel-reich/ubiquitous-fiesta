
def sim_prop_frac(n):
  gcd = lambda a, b: a if not b else gcd(b, a % b)
  return len(set(str(q//gcd(p, q))+'/'+str(p//gcd(p, q))
    for p in range(1, n+1) for q in range(1, p+1) if p != q))

