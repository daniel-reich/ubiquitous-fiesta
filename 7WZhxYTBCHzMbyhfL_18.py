
def knight_bfs(a, b, c, d):
  lst = [[a,b]]
  steps = 0
  while [c,d] not in lst:
    steps += 1
    temp = []
    for i in lst:
      temp+=[x for x in find_options(i[0],i[1]) if x not in lst]
    lst += temp
  return steps
    
def find_options(x,y):
  lst = []
  if x-1 > 0:
    if y-2 > 0:
      lst.append([x-1,y-2])
    if y+2 < 8:
      lst.append([x-1,y+2])
  if x+1 <= 8:
    if y-2 > 0:
      lst.append([x+1,y-2])
    if y+2 <= 8:
      lst.append([x+1,y+2])
  if x-2 > 0:
    if y-1 > 0:
      lst.append([x-2,y-1])
    if y+1 <= 8:
      lst.append([x-2,y+1])
  if x+2 <= 8:
    if y-1 > 0:
      lst.append([x+2,y-1])
    if y+1 <= 8:
      lst.append([x+2,y+1])
  return lst

