
from functools import reduce
def n_differences(lst):
  temp = lst
  for x in range(1, len(lst)):
    temp = [temp[y+1] - temp[y] for y in range(len(temp)-1)]
  return temp[0]

