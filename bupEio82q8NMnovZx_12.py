
def track_robot(instructions):
  instList = " ".join(instructions).split(" ")
  x, y = 0, 0
  for i in range(0, len(instList)):
    if instList[i]=="right": x = x + int(instList[i+1])
    if instList[i]=="left": x = x - int(instList[i+1])
    if instList[i]=="up": y = y + int(instList[i+1])
    if instList[i]=="down": y = y - int(instList[i+1])
  return [x, y]

