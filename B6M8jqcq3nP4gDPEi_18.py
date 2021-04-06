
def iso_group(lst):
  lst.sort()
  if len(lst)==1:
    return lst[0]
  if lst[0]==max(lst):
    return(lst)
  return iso_group(lst[1:] )

