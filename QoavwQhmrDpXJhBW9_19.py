
def flip_list(lst):
  dimension = get_dimension(lst)
  if dimension == 1:
    return [[i] for i in lst]
  elif dimension == 2:
    return [i for j in lst for i in j]
  else:
    return []
    
def get_dimension(lst):
  if not lst or not type(lst) is list:
    return 0
  dim = 1
  element = lst[0]
  while True:
    if not type(element) is list:
      break
    else:
      dim += 1
      element = element[0]
  return dim

