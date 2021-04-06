
def move_zeros(lst):
  res, zeros = [], 0
  for i in lst:
    if i == 0 and type(i) in [int, float]:
      zeros += 1
    else:
      res.append(i)
  return res + [0]*zeros

