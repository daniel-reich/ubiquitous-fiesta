
def sum_of_evens(lst):
  res = 0
  for i in lst:
    for j in i:
      if j%2==0:
        res += j
  return res

