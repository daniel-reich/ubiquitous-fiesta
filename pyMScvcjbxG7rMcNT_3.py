
def sum_list(lst):
  if type(lst[0]) != int and len(lst) == 1:
    return sum_list(lst[0])
  if type(lst[0]) != int:
    return sum_list(lst[0]) + sum_list(lst[1:])
  if len(lst) == 1:
    return lst[0]
  return lst[0] + sum_list(lst[1:])

