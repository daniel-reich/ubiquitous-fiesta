
def flip_list(lst):
  if len(lst) == 0:
    return lst
  elif isinstance(lst[0], list):
    return [item for sublist in lst for item in sublist]
  else:
    return [[i] for i in lst]

