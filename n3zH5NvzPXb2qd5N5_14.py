
def how_mega_is_it(n):
  a = abs(n)
  if a < 100:
    return "not a mega milestone"
  else:
    import math
    return (len(str(math.floor(a)))-2) * "MEGA " + "milestone"

