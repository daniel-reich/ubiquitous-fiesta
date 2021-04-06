
def relation_lst(lst):
  lst = sorted(lst)
  res = []
  for i, num in enumerate(lst):
    for j in range(i, len(lst)):
      res.append((num, lst[j]))
  return res

