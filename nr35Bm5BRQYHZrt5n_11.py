
def upward_trend(lst):
  if not all([isinstance(i, int) for i in lst]):
    return 'Strings not permitted!'
  return sorted(lst) == lst

