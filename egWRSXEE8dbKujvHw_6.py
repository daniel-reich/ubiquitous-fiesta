
def is_circle_collision(c1, c2):
  # create a line
  # if len(line) >= sum of radii, then overlap
  
  c1x = c1[1]
  c1y = c1[2]
  c2x = c2[1]
  c2y = c2[2]
  
  slope = 0
  if c1x - c2x != 0:
    slope = (c1y - c2y) / (c1x - c2x)
  else:
    slope = c1y - c2y
    
  trihyp = 0
  if slope > 0:
    trib = c2x - c1x
    trih = c2y - c1y
    trihyp = (trib**2 + trih **2)**.5
  elif slope < 0:
    trib = c1x - c2x
    trih = c1y - c2y
    trihyp = (trib**2 + trih**2)**.5
  else:
    if c1x > c2x:
      trihyp = c1x - c2x
    else:
      trihyp = c2x - c1x
  
  if c1[0] + c2[0] > trihyp:
    return True
  elif c1[0] + c2[0] < trihyp:
    return False
  else:
    return True

