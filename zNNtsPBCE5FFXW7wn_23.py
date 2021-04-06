
def empty_values(lst):
  l = []
  for i in lst:
    if type(i) == int:
      l.append(0)
    elif type(i) == float:
      l.append(0.0)
    elif type(i) == str:
      l.append('')
    elif type(i) == list:
      l.append([])
    elif type(i) == tuple:
      l.append(())
    elif type(i) == set:
      l.append(set())
    elif type(i) == bool:
      l.append(False)
    else:
      l.append(None)
  return l

