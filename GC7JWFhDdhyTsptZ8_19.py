
def sexy_primes(n, limit):
  p = [i for i in range(2, limit) if all([i%d != 0 for d in range(2, round(i**0.5)+1)])]
  pp = [(p[i], p[j]) for i in range(len(p)-1) for j in range(i+1, len(p)) if p[i]+6 == p[j]]
  pt = [(pp[i][0], pp[i][1], p[j])for i in range(len(pp)-1) for j in range(len(p)) if pp[i][1]+6 == p[j]]
  if n == 2:
    return pp
  return pt

