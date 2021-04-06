
def remove_smallest(lst):
  if len(lst)==0: return []
  else :lst.remove(min(lst))
  return lst

