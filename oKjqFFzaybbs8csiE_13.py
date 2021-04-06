
def cons(lst):
  nl = []
  x = sorted(lst)
  for y in range(min(lst), max(lst)+1):
    nl.append(y)
  if nl == x:
    return True
  else:
    return False

