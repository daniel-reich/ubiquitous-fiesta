
def remove_smallest(lst):
  if lst:
    minimum = min(lst)
    for index, item in enumerate(lst):
      if item == minimum:
        lst.pop(index)
        return lst
  else:
    return lst

