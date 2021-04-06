
def iso_group(lst):
  if len(lst) == 1:
    return lst[0]
  elif max(lst) == min(lst):
    return lst
  lst.remove(min(lst))
  return iso_group(lst)

