
def two_product(lst, n):
  for a in lst:
    for b in lst:
      if a*b==n:
        return sorted([a,b])

