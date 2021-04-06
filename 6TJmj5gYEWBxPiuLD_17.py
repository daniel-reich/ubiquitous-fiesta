
def seating_students(l):
  e = [x for x in range(1, l[0]+1) if x not in l[1:]]
  o = 0
  for x in e:
    if x+1 in e and x%2 == 1:
      o+=1
    if x+2 in e:
      o+=1
  return o

