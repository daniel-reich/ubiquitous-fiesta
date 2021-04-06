
import math
import re
def how_close_to_c(rapidity):
  ans = "{:.2e}".format(1/math.cosh(2*rapidity))
  return re.sub(r"-0", "-", ans)

