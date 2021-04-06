
def iso_group(lst):
  if len(set(lst)) == 1:
    return lst if len(lst) > 1 else lst[0]
  else:
    first = lst[0]
    i = 1
    while True:
      if lst[i] != first:
        break
      i += 1
    lst.remove(min(lst[i],first))
    return iso_group(lst)

