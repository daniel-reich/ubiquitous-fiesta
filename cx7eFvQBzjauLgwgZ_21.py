
def remove_smallest(lst):
  if len(lst) == 0:
    return []
  m = min(lst)
  lst.remove(m)
  return lst

