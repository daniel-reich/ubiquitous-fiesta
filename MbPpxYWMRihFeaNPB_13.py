
def sum_of_evens(lst):
  sumx = 0
  for i in lst:
    for x in i:
      if not x % 2:
        sumx = sumx + x
        
  return sumx

