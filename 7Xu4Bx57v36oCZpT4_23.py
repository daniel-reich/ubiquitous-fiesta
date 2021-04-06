
def where_is_waldo(lst):
  first = lst[0][0]
  for l in lst:
    for item in l:
      if item != first:
        return [lst.index(l)+1,l.index(item)+1]

