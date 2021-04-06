
def track_robot(instructions):
  pos = [0,0]
  for i in instructions:
    i=i.split()
    if i[0]=="left":
      pos[0]-=int(i[1])
    elif i[0]=="right":
      pos[0]+=int(i[1])
    elif i[0]=="down":
      pos[1]-=int(i[1])
    else:
      pos[1]+=int(i[1])
  return pos

