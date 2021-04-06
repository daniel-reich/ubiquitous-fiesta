
def simplify_sqrt(n):
  sq = []
  if n == 1:
    return (1, 1)
  else:
    for i in range(1, n):
      if n % (i**2) == 0:
        sq.append(i)
    a = sq[-1]
    b = n//(a**2)
    return (a, b)

