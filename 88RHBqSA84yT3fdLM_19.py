
def inator_inator(inv):
  return inv[-1].casefold() in "aiueo" and "{}-inator {}000".format(inv, len(inv)) or "{}inator {}000".format(inv, len(inv))

