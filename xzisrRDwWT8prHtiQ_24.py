
def difference_two(lst):
  new_list = []
  for i in lst:
    if i + 2 in lst:
      x = [i, i + 2]
      new_list.append(x)
  new_list.sort()
  return new_list

