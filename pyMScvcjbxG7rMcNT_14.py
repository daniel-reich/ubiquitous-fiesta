
def sum_list(lst):
  if not lst:
    return 0
  elif type(lst[-1])==int:
    return lst[-1] + sum_list(lst[:-1])
  else:
    return sum_list(lst[-1]) + sum_list(lst[:-1])

