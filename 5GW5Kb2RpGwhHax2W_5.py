
def spiral_transposition(lst):
  l = []
  l.extend(lst[0])
  col1 = []
  for i in range(1,len(lst)-1):
    col1.append(lst[i][-1])
  l.extend(col1)
  l.extend(lst[-1][::-1])
  col2 = []
  for i in range(1,len(lst)-1):
    col2.append(lst[i][0])
  col2.reverse()
  l.extend(col2)
  if len(lst) > 2 and len(lst[1])>2:
    new = [r[1:-1] for r in lst[1:-1]]
    l1 = spiral_transposition(new)
    if len(lst) == 3:
      l1 = l1[:-1]
    l.extend(l1)
  return l

