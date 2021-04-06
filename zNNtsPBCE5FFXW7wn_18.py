
def empty_values(lst):
  emptied = []
  for item in lst:
    if type(item) is str:
      emptied.append("")
    elif type(item) is int:
      emptied.append(0)
    elif type(item) is float:
      emptied.append(0.0)
    elif type(item) is bool:
      emptied.append(False)
    elif type(item) is list:
      emptied.append([])
    elif type(item) is tuple:
      emptied.append(tuple())
    elif type(item) is set:
      emptied.append(set())
    else:
      emptied.append(None)
      
  return emptied

