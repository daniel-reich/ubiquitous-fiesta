
def sum_two_smallest_nums(lst):
  min1, min2 = float('+inf'), float('+inf')
  ind1 = 0
  for i in range(len(lst)):
    if lst[i] >= 0:
      if lst[i] < min1:
        min1 = lst[i]
        ind1 = i
  for i in range(len(lst)):
    if lst[i] >= 0 and i != ind1:
        if lst[i] < min2:
          min2 = lst[i]
  return min1 + min2

