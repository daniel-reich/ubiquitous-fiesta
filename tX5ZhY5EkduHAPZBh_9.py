
def nearest_element(n, lst):
  near=abs(n-lst[0])
  number=lst[0]
  for x in lst:
    if abs(n-x)<near:
      near=abs(n-x)
      number=x
    elif abs(n-x)==near:
      if x>number:
        number=x
  return lst.index(number)

