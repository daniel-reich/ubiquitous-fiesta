
def count_boomerangs(lst):
  result = []
  for i in range(len(lst)-2):
    if lst[i] == lst[i+2] and lst[i] != lst[i+1]:
      result.append([lst[i], lst[i+1], lst[i+2]])
  return len(result)

