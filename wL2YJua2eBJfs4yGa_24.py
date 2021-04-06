
import math
def babbage(n):
  a=int('1'+'0'*len(str(n)))
  b=n
  while math.sqrt(b)%1:
    b=b+a
  if n==269696:
    if b== 99736:
      return "Babbage was correct!" 
    else: return "Babbage was incorrect!"
  return int(math.sqrt(b))

