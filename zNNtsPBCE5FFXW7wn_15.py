
def empty_values(lst):
  a = []
  for i in lst:
    if type(i) == str:
      a.append("")
    elif type(i) == int:
      a.append(0)
    elif type(i) == float:
      a.append(0.0)
    elif type(i) == bool:
      a.append(False)
    elif type(i) == list:
      a.append([])
    elif type(i) == set:
      a.append(set())
    elif type(i) == tuple:
      a.append(())
    else:
      a.append(None)
  return a

