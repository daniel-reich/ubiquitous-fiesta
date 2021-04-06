
def makeBox(n):
  if n == 1:
    return ["#"]
  
  topbot, middle, box = "", "", []
  for i in range(n):
    topbot += "#"
  
  middle += "#"
  for j in range(n-2):
    middle += " "
  middle += "#"
  
  box = [topbot]
  for k in range(n-2):
    box += [middle]
  box += [topbot]
  return box

