
def complete_square(lst):
  utd = len(lst)
  ltr = len(lst[0])
  if ltr == utd:
    return lst
  elif ltr > utd:
    adding = ltr - utd
    c = []
    for x in range(ltr):
      c.append(0)
    for x in range(adding):
      lst.append(c)
  else:
    for x in range(utd - ltr):
      for i in lst:
        i.append(0)
  return lst

