
from functools import reduce
def total_volume(*boxes):
  a=0
  for i in boxes:
    res=reduce(lambda a,b:a*b,i)
    a=a+res
  return a

