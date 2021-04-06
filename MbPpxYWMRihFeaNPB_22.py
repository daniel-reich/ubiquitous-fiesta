
def sum_of_evens(lst):
  ret = 0
  for i in lst:
    for j in i:
      if j % 2 == 0:
        ret = ret + j
  return ret

