
def flip_list(lst):
  if lst == []:
    return []
  elif type(lst[0]) is int:
    return [[x] for x in lst]
  else:
    return [x for sub in lst for x in sub]

