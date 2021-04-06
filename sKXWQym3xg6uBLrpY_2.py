
from statistics import median
def iqr(lst):
  lst.sort()
  Q1=lst[:len(lst)//2]
  Q3=lst[(1-len(lst))//2:]
  med=median(lst)
  return median(Q3)-median(Q1)

