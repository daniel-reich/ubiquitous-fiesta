
def combinations(*items):
  print(items)
  a = 1
  for i in items:
    if i != 0:
      a = a*i
  return a

