
def iso_group(lst):
  if len(set(lst)) != 1:
    lst.pop(lst.index(min(lst)))
    return iso_group(lst)
  return lst[0] if len(lst)==1 else lst

