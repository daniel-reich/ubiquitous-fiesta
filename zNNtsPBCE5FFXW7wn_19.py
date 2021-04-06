
def empty_values(lst):
  lst2 = []
  for i in lst:
    if type(i) == int:
      lst2.append(0)
    elif type(i) == float:
      lst2.append(0.0)
    elif type(i) == str:
      lst2.append('')
    elif type(i) == bool:
      lst2.append(False)
    elif type(i) == list:
      lst2.append([])
    elif type(i) == tuple:
      lst2.append(())
    elif type(i) == set:
      lst2.append(set())
    else:
      lst2.append(None)
  return lst2

