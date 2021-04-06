
def sum_list(lst):
  if lst == []:
    return 0
  elif type(lst[0])== list:
    return sum_list(lst[0])+sum_list(lst[1:])
  else:
    return lst[0]+sum_list(lst[1:])

