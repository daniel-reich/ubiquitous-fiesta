
def remove_smallest(lst):
  if len(lst)>0:
    smol=min(lst)
    lst.remove(smol)
  return lst

