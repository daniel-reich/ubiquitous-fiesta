
def parallel_resistance(lst):
  c=0
  for i in lst:
    c+=1/i
  b=round(1/c,1)
  return b

