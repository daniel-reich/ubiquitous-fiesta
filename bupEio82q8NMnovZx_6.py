
def track_robot(instructions):
  x=0
  y=0
  directions=[]
  distances=[]
  num=0
  for i in instructions:
    i=i.replace('right','r')
    i=i.replace('left','l')
    i=i.replace('up','u')
    i=i.replace('down','d')
    directions.append(i[0])
    distances.append(i[2:])
  for i in directions:
    if(i=='r'):
      x+=int(distances[num])
    elif(i=='l'):
      x-=int(distances[num])
    elif(i=='u'):
      y+=int(distances[num])
    elif(i=='d'):
      y-=int(distances[num])
    num+=1
  return [x,y]

