
import numpy as np
def polygon(lst):
  Ox, Oy = (sum(coor[0] for coor in lst)/len(lst),sum(coor[1] for coor in lst)/len(lst))
  lst = sorted(lst,key=lambda x: np.angle(complex(x[0]-Ox,x[1]-Oy)))
  v1 = sum(lst[i][0]*lst[(i+1)%len(lst)][1] for i in range(len(lst)))
  v2 = sum(lst[i][1]*lst[(i+1)%len(lst)][0] for i in range(len(lst)))
  return (v1-v2)/2

