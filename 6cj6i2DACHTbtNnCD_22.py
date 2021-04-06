
def two_product(lst, n):
  for x in lst:
    if n%x==0 and n//x in lst:
      return sorted([x,n//x])

