
def accumulating_product(lst):
  res = []
  for i in range(1, len(lst)+1):
    exp = "*".join(str(j) for j in lst[:i])
    res.append(eval(exp))
  return res

