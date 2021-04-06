
import math
def largest_exponential(lst):
  reslog10=[math.log10(base)*exp for base,exp in lst]
  return reslog10.index(max(reslog10))+1

