
def how_mega_is_it(n):
  import math
  if abs(n) < 100:
    return "not a mega milestone"
  else:
    k = int(abs(n))
    return (len(str(k))-2)*"MEGA " + "milestone"

