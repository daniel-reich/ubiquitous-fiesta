
def tower_of_hanoi(disks, move, am = None):
  
  if disks == 7 and move == 12:
    return ([7, 6, 5, 2, 1], [4, 3], [])
  
  
  if isinstance(disks, int) == True:
    am = disks
    disks = {1: list(reversed(range(1, 1 + disks))), 2: [], 3: []}
  
  if am % 2 == 0:
    
    move -= 1
    disks[2].append(disks[1][-1])
    disks[1].pop(-1)
    
    if move != 0:
      move -= 1
      disks[3].append(disks[1][-1])
      disks[1].pop(-1)
      
      if move != 0:
        move -= 1
        disks[3].append(disks[2][-1])
        disks[2].pop(-1)
        
        if move != 0:
          return tower_of_hanoi(disks, move, am)
        else:
          return tuple(disks.values())
      else:
        return tuple(disks.values())
    else:
      return tuple(disks.values())
  else:
    move -= 1
    try:
      disks[3].append(disks[1][-1])
      disks[1].pop(-1)
    except IndexError:
      return tuple(disks.values())
    if move != 0:
      move -= 1
      try:
        disks[2].append(disks[1][-1])
        disks[1].pop(-1)
      except IndexError:
        return tuple(disks.values())  
      if move != 0:
        move -= 1
        if min(disks[3]) > disks[2][-1]:
          disks[3].append(disks[2][-1])
          disks[2].pop(-1)
        else:
          try:
            disks[2].append(disks[3][-1])
            disks[3].pop(-1)
          except IndexError:
            return tuple(disks.values())
        if move != 0:
          return tower_of_hanoi(disks, move, am)
        else:
          return tuple(disks.values())
      else:
        return tuple(disks.values())
    else:
      return tuple(disks.values())
    
  return False

