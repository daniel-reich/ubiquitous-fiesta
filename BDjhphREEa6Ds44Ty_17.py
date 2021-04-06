
from math import sqrt
def d(x,y,a,b):
  return sqrt((x-a)**2+(y-b)**2)
def bomb(lst):
  for j in range(55):
    for k in range(55):
      for i in lst:
        if not(d(i[0],i[1],j,k)>0.343*i[2]-0.05 and d(i[0],i[1],j,k)<0.343*i[2]+0.05):
          break
      else:
        return(j,k)

