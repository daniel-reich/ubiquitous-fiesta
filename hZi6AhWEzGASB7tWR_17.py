
def check(lst):
  if len(set(lst)) != len(lst):
    return 'neither'
  if sorted(lst) == lst:
    return 'increasing'
  elif sorted(lst)[::-1] == lst:
    return 'decreasing'
  return 'neither'

