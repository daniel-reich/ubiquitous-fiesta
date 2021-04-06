
def pluralize(lst):
  new_list = []
  for i in lst:
    if lst.count(i) > 1:
      new_list.append(i+'s')
    else:
      new_list.append(i)
  return set(new_list)

