
def pluralize(lst):
  res = []
  for i in lst:
    if lst.count(i) > 1 and i not in res:
      res.append(i + 's')
    else:
      res.append(i)
  return set(res)

