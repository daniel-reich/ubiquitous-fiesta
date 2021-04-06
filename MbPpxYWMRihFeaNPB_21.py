
def sum_of_evens(lst):
  res = 0
  for x in lst:
    for y in x:
      if(not y%2):
        res += y
  return res

