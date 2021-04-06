
def is_ladder_safe(ldr):
  
  length = len(ldr[0]) >= 5
  
  if length == False:
    return False
  
  rungs = []
  
  for n in range(0, len(ldr)):
    lyr = ldr[n]
    
    c = lyr.count('#')
    if c > 2:
      if len(lyr) != c:
        return False
      else:
        rungs.append(n)
  
  d = []
  
  if len(rungs) < 1:
    return False
  
  for n in range(1, len(rungs)):
    r1 = rungs[n-1]
    r2 = rungs[n]
    
    d.append(r2-r1)
  
  if d[0] > 3:
    return False
  if d.count(d[0]) != len(d):
    return False
  return True

