
def track_robot(instructions):
  l=[]
  x=0
  y=0
  for j in instructions :
    l.append(j.split())
​
  for k in l:
    if k[0]=="left":
      x=x-int(k[1])
    elif k[0]=="right":
      x=x+int(k[1])
    elif k[0]=="up":
      y=y+int(k[1])
    elif k[0]=="down":
      y=y-int(k[1])
  
  return [x,y]

