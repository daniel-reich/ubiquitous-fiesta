
def relation_lst(lst):
  lst = sorted(lst)
  res = []
  for a in lst:
    for b in lst:
      if a <= b:
        res.append((a, b))
  return res

