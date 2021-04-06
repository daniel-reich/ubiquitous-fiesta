
gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
def sim_prop_frac(n):
  foo = 0
  for i in range(2, n + 1):
    for j in range(1, i):
      if gcd(i, j) == 1:
        foo += 1
  return foo

