
def change_types(lst):
  res = []
  for l in lst:
    if type(l) == int:
      if not l&1:
        l += 1
      res.append(l)
    elif type(l) == bool:
      res.append(not l)
    elif type(l) == str:
      res.append((l+'!').capitalize())
  return res

