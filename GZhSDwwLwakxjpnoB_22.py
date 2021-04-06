
def thirdthird(lst):
  if len(lst) < 3:
    return False
  s = lst[2]
  if len(s) < 3:
    return False
  return s[2]

