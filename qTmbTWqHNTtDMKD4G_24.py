
import queue
import numpy as np
def get_path_length(world, width, height):
  world=world.replace(",","")
  q = queue.Queue(width*height)
  M=np.zeros((width+2,height+2),dtype=type('a'))
  D=-np.ones(M.shape,dtype=np.int)
  M[:]='t'
  for x in range(width):
    for y in range(height):
      M[x+1,y+1]=world[y*width+x]
      if(M[x+1,y+1]=='m'):
        q.put((x+1,y+1))
        D[x+1,y+1]=0
  while not q.empty():
    x,y=q.get()
    for d in range(9):
      dx,dy=(d%3)-1,d//3-1
      if(M[x+dx,y+dy]=='h'):
        return D[x,y]+1
      elif((M[x+dx,y+dy]=='.') and D[x+dx,y+dy]<0 ):
        q.put((x+dx,y+dy))
        D[x+dx,y+dy]=D[x,y]+1
  return -1

