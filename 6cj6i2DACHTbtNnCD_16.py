
def two_product(lst, n):
  from itertools import permutations
  a = permutations(lst,2)
  for x in list(a):
    if x[1] * x[0] == n:
      return list(sorted(x))
    else:
      pass
  return None

