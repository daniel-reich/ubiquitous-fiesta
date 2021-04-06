
def remove_smallest(lst):
  if lst == []:
    return []
  min_value = min(lst)
  lst.remove(min_value)
  return lst

