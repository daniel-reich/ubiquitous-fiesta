
def list_values_types(lst):
  result = []
  for e in lst:
    result.append(str(type(e))[8:-2])
  return result

