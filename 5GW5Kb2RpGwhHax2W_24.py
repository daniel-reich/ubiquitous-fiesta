
def spiral_transposition(lst):
  if not lst:
    return []
  lst1 = lst[0]
  del lst[0]
  lst2 = []
  if len(lst) > 0:
    for i in lst[:-1]:
      lst1.append(i[-1])
      lst2.append(i[1:-1])
    lst1 += lst[-1][::-1]
    del lst[-1]
    for i in lst[::-1]:
      lst1.append(i[0])
  return lst1 + spiral_transposition(lst2)

