
def iso_group(lst):
  if len(lst) == 1:
    return lst[0]
  if len(set(lst)) == 1:
    return lst
  if min(lst) != max(lst):
    lst.remove(min(lst))
  return iso_group(lst)

