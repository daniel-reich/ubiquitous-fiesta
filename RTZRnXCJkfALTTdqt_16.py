
def sum_neg(lst):
  pos = 0
  neg = 0
  if lst == []:
    return lst
  for caca in lst:
    if caca > 0:
      pos += 1
    else:
      neg += caca
  return [pos,neg]

