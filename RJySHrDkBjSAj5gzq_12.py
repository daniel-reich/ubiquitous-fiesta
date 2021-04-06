
import math
def nespers(lst):
  a = math.factorial(len(lst))
  b = 1
  nesper1 = list(filter(lambda x: isinstance(x,list), lst))
  for i in nesper1:
    nesper1 += list(filter(lambda x: isinstance(x,list), i))
  
  lstlen = list(map(lambda x : len(x), nesper1))
  
  for i in range(0, len(lstlen)) :
    b *= math.factorial(lstlen[i])
    
  return a*b

