
def check(lst):
  newlst = list(set(lst))
  if lst == sorted(newlst):
    return 'increasing'
  elif lst[::-1] == sorted(newlst):
    return 'decreasing'
  else:
    return 'neither'

