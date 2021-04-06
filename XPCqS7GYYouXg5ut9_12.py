
def simplify_sqrt(n):
  k = 2 
  while k ** 2 < n and n % (k**2) != 0:
    k += 1
  if n % (k**2) == 0:
    sq = simplify_sqrt(n / (k ** 2) )
    return (k * sq[0], sq[1])
  else:
    return (1, n)

