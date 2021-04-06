
import math
def largest_exponential(lst):
  for i in range(len(lst)):
    lst[i] = (lst[i][1])*math.log(lst[i][0])
  return lst.index(max(lst))+1

