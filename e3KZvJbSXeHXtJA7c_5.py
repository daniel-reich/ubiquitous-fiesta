
def sum_missing_numbers(lst):
  lst = sorted(lst)
  min_range = lst[0]
  max_range = lst[-1]
  total = 0
  if min_range > max_range:
    for eachnumber in range(max_range,min_range+1):
      if eachnumber not in lst:
        total += eachnumber
    print(total)
  else:
    for eachnumber in range(min_range,max_range+1):
      if eachnumber not in lst:
        total += eachnumber
    return total

