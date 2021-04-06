
def check_pattern(lst, pattern):
  res1 = {}
  res2 = {}
  for l, c in zip(lst, pattern):
    res1.setdefault(c, set()).add(tuple(l))
    res2.setdefault(tuple(l), set()).add(c)
  return all(len(x) == 1 for x in res1.values()) and all(len(x) == 1 for x in res2.values())

