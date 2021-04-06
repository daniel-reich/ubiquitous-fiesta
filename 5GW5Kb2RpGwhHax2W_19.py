
def spiral_transposition(lst):
  if len(lst) == 1:
    return lst[0]
  elif len(lst) == 0:
    return lst
​
  r = []
  l = []
  for i in lst[1:-1]:
    l.append(i.pop(0))
    r.append(i.pop(-1))
​
  return lst.pop(0)+r+lst.pop(-1)[::-1]+l[::-1] + spiral_transposition(lst)

