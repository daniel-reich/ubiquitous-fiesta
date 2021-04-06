
def remove_smallest(lst):
  if len(lst) == 0:
    return lst
  else:
    lst.remove(min(lst))
    return lst

