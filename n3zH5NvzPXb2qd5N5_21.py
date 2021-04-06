
def how_mega_is_it(n):
  n = abs(int(n))
  if n<100:
    return "not a mega milestone"
  return (len(str(n)) - 2)*"MEGA " + "milestone"

