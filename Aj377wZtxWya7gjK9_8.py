
def sum_missing_numbers(lst):
  sum =0
  ma = max(lst)
  mi = min(lst)
  for i in range(mi,ma+1):
    if((i in lst)==True):
      pass
    else:
      sum = sum + i
  return sum

