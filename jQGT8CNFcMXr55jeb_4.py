
def numbers_sum(lst):
  
  k=0
  for thing in lst:
    if type(thing) == int:
      k+=thing
  return k

