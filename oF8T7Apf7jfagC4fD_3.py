
def antipodes_average(lst):
  if len(lst) % 2 != 0:
    lst.pop(len(lst)//2)
  res = []
  for i in range(len(lst)//2):
    res.append((lst[i] + lst[-i-1]) / 2)
  return res

