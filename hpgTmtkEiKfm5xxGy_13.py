
def paths(x, y):
  if [x,y]==[0,0]:
    return 1
  p = [[0,1],[1,0],[0,-1],[-1,0]]
  return sum([paths(x+i[0],y+i[1]) for i in p if dist(x+i[0],y+i[1])<=dist(x,y)])
  
def dist(x,y):
  return (x**2+y**2)**(1/2)

