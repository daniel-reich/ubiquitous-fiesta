
def left_slide(row):
  r = [x for x in row if x != 0]
  lst = []
​
  while len(r) >= 2:
    a,b, *c = r
    if a == b:
      lst.append(a * 2)
      r = c
    else:
      lst.append(a)
      r = [b]+c
  if len(r) == 1:
    lst.append(r[0])
  while len(lst) < len(row):
    lst.append(0)
  return lst

