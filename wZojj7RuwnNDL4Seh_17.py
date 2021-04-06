
def completely_filled(lst):
  if len(lst) <= 2:
    return True
  lst = lst[1:-1]
  NL = ''
  for i in lst:
    NL += i
  if ' ' in NL:
    return False
  else:
    return True

