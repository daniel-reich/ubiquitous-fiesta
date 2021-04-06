
def move_to_end(lst, el):
  list_non_el = []
  list_el = []
  for i in lst:
    if i == el:
      list_el.append(i)
    else:
      list_non_el.append(i)
  return list_non_el + list_el

