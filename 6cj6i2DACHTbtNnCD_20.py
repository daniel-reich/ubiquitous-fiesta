
def two_product(lst, n):
  for i in lst:
      if i!=0 and n/i in lst:
          return sorted([i, n//i])
  return None

