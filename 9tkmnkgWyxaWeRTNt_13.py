
import math
def median(lst):
  lst = sorted(lst)
  
  if len(lst)%2!=0:
    return lst[len(lst)//2]
  else:
    return (lst[len(lst)//2-1]+lst[len(lst)//2])/2

