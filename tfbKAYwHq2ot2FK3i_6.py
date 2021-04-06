
import math
def non_repeats(base):
  if not isinstance(base, int) or base<=1:
     return 'Error'
  pl=[(base-1)*math.factorial(base-1)//math.factorial(base-n) for n in range(1,base+1)]
  return sum(pl)

