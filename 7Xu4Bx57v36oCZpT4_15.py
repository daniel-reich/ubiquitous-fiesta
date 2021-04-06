
def where_is_waldo(lst):
  nl = []
  for x in range(len(lst)):
    for y in range(len(lst[x])):
      if lst[0][0] != lst[x][y]:
        nl.append(x +1)
        nl.append(y +1)
  return nl

