
import math
​
def DECIMATOR(txt):
  x = math.ceil(len(txt)/10)
  return(txt[:-x])

