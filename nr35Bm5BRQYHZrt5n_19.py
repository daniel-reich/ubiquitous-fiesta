
def upward_trend(lst):
  for i in lst:
    if isinstance(i, str) == True:
      return "Strings not permitted!"
  if lst == sorted(lst):
    return True
  if lst != sorted(lst):
    return False

