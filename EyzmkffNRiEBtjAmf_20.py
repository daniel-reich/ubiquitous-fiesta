
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
import math
def does_brick_fit(a,b,c, w,h):
  if max(a,b,c)==c:
    return math.sqrt(a**a+b**b)<= math.sqrt(w**w+h**h)
  if max(a,b,c)==b:
    return math.sqrt(a**a+c**c)<= math.sqrt(w**w+h**h)
  else:
    return math.sqrt(c**c+b**b)<= math.sqrt(w**w+h**h)

