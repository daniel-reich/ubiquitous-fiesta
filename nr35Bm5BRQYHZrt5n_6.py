
def upward_trend(lst):
  for i in lst:
    if isinstance(i, str):
      return "Strings not permitted!"
  for i, j in enumerate(lst[:-1]):
    if j >= lst[i + 1]:
      return False
  return True

