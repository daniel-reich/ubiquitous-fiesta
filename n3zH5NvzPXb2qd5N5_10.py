
def how_mega_is_it(n):
  return "not a mega milestone" if abs(n) < 100 else "MEGA "*len(str(int((abs(n)//100)))) + "milestone"

