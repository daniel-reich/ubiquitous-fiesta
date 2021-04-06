
def sum_primes(lst):
  i= [2,3,5,7]
  retorn = []
  for x in lst:
    if x!=1:
      retorn.append(x)
    for c in i:
      if x % c == 0 and x != c:
        retorn.pop(-1)
        break
  return sum(retorn) if len(lst) > 0 else None

