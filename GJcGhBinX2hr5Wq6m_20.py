
def move_zeros(lst):
  others, zeros = [], []
  for x in lst:
    if (type(x) == int or type(x) == float) and x == 0:
      zeros.append(0)
    else:
      others.append(x)
  return others + zeros

