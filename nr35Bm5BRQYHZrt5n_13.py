
def upward_trend(lst):
  l = []
  for x in lst:
    if not isinstance(x, int):
      return "Strings not permitted!"
    l.append(x)
  l.sort()
  return l == lst

