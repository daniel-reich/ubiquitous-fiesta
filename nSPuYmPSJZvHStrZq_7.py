
def oddeven(lst):
  e = []
  o = []
  for i in lst:
    if i%2 == 0:
      e.append(i)
    else:
      o.append(i)
  if len(o) > len(e):
    return True
  return False

