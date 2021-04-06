
import math
def num_layers(n):
  def x(n):
    if n==0:
      return 0.0005
    else:
      return x(n-1)*2
  return str(x(n))+"m"

