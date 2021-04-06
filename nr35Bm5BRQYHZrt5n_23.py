
def upward_trend(lst):
  for i in range(1, len(lst)):
    if isinstance(lst[i], str):
      return "Strings not permitted!"
    elif lst[i] <= lst[i-1]:
      return False
  else:
    return True

