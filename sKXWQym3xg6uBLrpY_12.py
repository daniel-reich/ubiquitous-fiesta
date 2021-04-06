
from statistics import median
​
def iqr(lst):
  lst.sort()
  return median(lst[(len(lst)+1)//2:]) - median(lst[:len(lst)//2])

