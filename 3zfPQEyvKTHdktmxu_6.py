
def big_sub(lst):
  res = [0, 0, 0]
  sum = 0
  for cpos, val in enumerate(lst):
    if sum <= 0:
      spos =  cpos
      sum = val
    else:
      sum += val
    if sum >= res[0]:
      res[0], res[1], res[2] = sum, spos, cpos
  return res

