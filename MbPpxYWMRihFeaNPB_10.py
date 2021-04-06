
def sum_of_evens(lst):
  total = 0 
  for series in lst:
    for ele in series:
      if not (ele % 2): total += ele
  return total

