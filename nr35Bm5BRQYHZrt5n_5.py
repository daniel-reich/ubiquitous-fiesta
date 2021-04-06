
def upward_trend(lst):
  for i in lst:
    if isinstance(i,str):
      return r'Strings not permitted!'
  return sorted(lst) == lst

