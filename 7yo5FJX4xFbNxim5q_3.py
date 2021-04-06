
def harry(po,x=0,y=0):
  if x>len(po)-1 or y>len(po[x])-1:
    return -1
  if x==len(po)-1 and y==len(po[x])-1:
    return po[x][y]
  return po[x][y]+max([harry(po,x+i[0],y+i[1]) for i in [[0,1],[1,0]]])

