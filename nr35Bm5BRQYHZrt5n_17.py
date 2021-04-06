
def upward_trend(lst):
  first = lst[0]
  for el in lst:
    if isinstance(el, str):
      return "Strings not permitted!"
    else:
      if el < first:
        return False
      else:
        first = el
  return True

