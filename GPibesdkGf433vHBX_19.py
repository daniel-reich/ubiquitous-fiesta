
prime=[2]
def goldbach_conjecture(n):
  if n%2:
    return []
  global prime
  if prime[-1]<n:
    for i in range(prime[-1]+1,n+1):
      if all(i%p for p in prime):
        prime.append(i)
  for p in prime:
    if (n-p) in prime:
      return [p,n-p]

