
def remove_smallest(lst):
  if lst:
    x = min(int(s) for s in lst)
    lst.remove(x)
  return lst

