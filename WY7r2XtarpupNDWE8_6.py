
def tower_of_hanoi(disks, move):
  towers = (list(range(disks,0,-1)),[],[])
  if disks % 2 == 0:
    coords = {0: (1,2),1:(1,3)}
  else:
    coords = {0: (1,3),1:(1,2)}
  coords[2] = (2,3)
  for k in range(0,move):
    i,j = coords[k%3][0]-1, coords[k%3][1]-1
    try:
      if towers[i][-1] > towers[j][-1]:
        j,i = i,j
    except IndexError:
      if not towers[i]:
        j,i = i,j
    towers[j].append(towers[i][-1])
    towers[i].pop()
      
  return towers

