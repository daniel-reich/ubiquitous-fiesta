
from re import *
def grab_number_sum(s):
  s = findall(r"\d+",s)
  return sum(int(i) for i in s)

