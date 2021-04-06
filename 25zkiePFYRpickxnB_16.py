
def count_boomerangs(lst):
  result = 0
  if len(lst) < 3:
    return 0
  for i in range(len(lst) - 2):
    if (lst[i] == lst[i+2] and lst[i] != lst[i+1]):
      result += 1
  return result

