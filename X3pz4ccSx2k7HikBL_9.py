
def showdown(p1, p2):
  plen,p2len = 0,0
  for char in p1:
    if char == " ":
      plen+=1
    else:
      break
  for char in p2:
    if char == " ":
      p2len+=1
    else:
      break
  if plen<p2len:
    return "p1"
  elif plen>p2len:
    return "p2"
  else:
    return "tie"

