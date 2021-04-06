
def remove_smallest(lst):
  if len(lst) <= 1:
    return []
  pos = lst.index(min(lst)) 
  return lst[:pos] + lst[pos + 1:]

