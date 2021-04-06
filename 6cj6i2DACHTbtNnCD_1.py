
def two_product(lst, n):
  return ([sorted([i, n/i]) for i in lst if i and n/i in lst] or [None])[0]

