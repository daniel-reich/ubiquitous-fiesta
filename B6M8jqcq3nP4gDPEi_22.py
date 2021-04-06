
def iso_group(lst):
  lst2 = []
  for elem in lst:
    if lst2 == []:
      lst2.append(elem)
    elif elem > lst2[0]:
      lst2.pop()
      lst2.append(elem)
    elif elem == lst2[0]:
      lst2.append(elem)
  if len(lst2) > 1:
    return lst2
  else:
    return lst2[0]

