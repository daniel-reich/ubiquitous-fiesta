
def unique_lst(lst):
  new_list = []
  for elem in lst:
    if elem > 0 and elem not in new_list:
      new_list.append(elem)
  return new_list

