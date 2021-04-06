
import numpy as np
def complete_square(lst):
  lst = np.array(lst)
  def squarify(M,val=0):
    (a,b)=M.shape
    if a>b:
      padding=((0,0),(0,a-b))
    else:
      padding=((0,b-a),(0,0))
    return np.pad(M,padding,mode='constant',constant_values=val)  
  return squarify(lst).tolist()

