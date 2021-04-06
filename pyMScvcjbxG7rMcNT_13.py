
def sum_list(lst):
  if isinstance(lst[0],int):
    if len(lst)>1:
      return lst[0]+sum_list(lst[1:])
    else:
      return lst[0]
  else:
    if len(lst)>1:
      return sum_list(lst[0])+sum_list(lst[1:])
    else:
      return sum_list(lst[0])

