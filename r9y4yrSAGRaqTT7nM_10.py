
def find_missing(lst):
  try:
    if [] in lst:
      return False
    l = [len(i) for i in lst]
    for i in range(min(l),max(l)):
      if i not in l:
        return i
  except (TypeError, ValueError):
    return False

