
def inator_inator(inv):
  infix = "-inator " if inv[-1] in "aeiouAEIOU" else "inator "
  return inv + infix + str(len(inv)) + "000"

