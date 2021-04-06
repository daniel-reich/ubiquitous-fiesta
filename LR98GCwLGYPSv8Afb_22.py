
def pluralize(lst):
  res = set()
  seen = []
  for i in lst:
    if i not in seen:
      seen.append(i)
      res.add(i + 's' if lst.count(i) > 1 else i)
  return res

