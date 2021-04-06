
def add_indexes(lst):
  index = 0
  new_list = []
  for i in lst:
    new_list.append(i + index)
    index += 1
  return new_list

