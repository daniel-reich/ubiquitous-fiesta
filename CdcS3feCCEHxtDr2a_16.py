
def clear_ordering(lst):
  t1 = []
  t2 = []
  for i in range(len(lst)):
    t1.append(lst[i][0])
    t2.append(lst[i][1])
  c1 = 0
  for i in range(len(t1)):
    if t1[i] not in t2:
      c1 += 1
  c2 = 0
  for i in range(len(t2)):
    if t2[i] not in t1:
      c2 += 1
  if c1 > 1 or c2 > 1:
    return False
  else:
    return True

