
def numbers_to_ranges(lst):
  if lst == []:
    return []
  curr = lst[0]
  ranges = []
  for i in range(len(lst)-1):
    if lst[i] != lst[i+1]-1:
      ranges.append(str(curr) + (curr != lst[i])*('-' + str(lst[i])))
      curr = lst[i+1]
  ranges.append(str(curr) + (curr != lst[-1])*('-' + str(lst[-1])))
  return ranges

