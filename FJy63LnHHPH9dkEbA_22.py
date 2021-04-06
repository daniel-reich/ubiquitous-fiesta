
import math
def how_close_to_c(rapidity):
  a=1/(math.cosh(2*rapidity))
  b=str("{:.2e}".format(a))
  c=b.split("-")
  d=len(c[1])
  if(c[1][0]=="0"):
    return c[0]+"-"+c[1][1:]
  else:
    return b

