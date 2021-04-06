
def seating_students(lst):
  k = lst[0]
  r1 = [0 for n in range(k//2)]
  r2 = [0 for n in range(k//2)]
  for i,w in enumerate(lst):
    if i==0:
      continue
    if w%2 == 0:
      r2[w//2-1] = 1
    else:
      r1[w//2] = 1
  erg = 0
  for i in range(len(r1)-1):
    if r1[i]==0 and r2[i]==0:
      erg += 1
    if r1[i]==0 and r1[i+1]==0:
      erg += 1
    if r2[i]==0 and r2[i+1]==0:
      erg += 1
  if r2[len(r1)-1]==0 and r1[len(r1)-1]==0:
    erg += 1
  return erg

