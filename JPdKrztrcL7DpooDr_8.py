
def collatz(n):
  M = n
  it = 0
  while n!=1:
    if n%2: n = 3*n+1
    else: n//= 2
    it+= 1
    M = max(n,M)
  return [it,M]

