
def remove_smallest(lst):
  lst if len(lst) < 1 else lst.remove(min(lst))
  return lst

