
def empty_values(lst):
  result = []
  for value in lst:
    if type(value) == int:
      result.append(0)
    elif type(value) == float:
      result.append(0.0)
    elif type(value) == str:
      result.append("")
    elif type(value) == bool:
      result.append(False)
    elif type(value) == list:
      result.append([])
    elif type(value) == tuple:
      result.append(())
    elif type(value) == set:
      result.append(set())
    else:
      result.append(None)
  return result

