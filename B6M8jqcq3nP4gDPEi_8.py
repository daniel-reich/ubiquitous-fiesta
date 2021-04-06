
def iso_group(lst):
  if len(set(lst))==1:
    return lst if len(lst)>1 else lst[0]
  return iso_group(lst[1:]+[lst[0]]) if lst[0]==max(lst) else iso_group(lst[1:])

