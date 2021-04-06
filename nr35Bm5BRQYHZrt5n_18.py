
def upward_trend(lst):
  return 'Strings not permitted!' if any(type(i)==str for i in lst) else lst == sorted(lst)

