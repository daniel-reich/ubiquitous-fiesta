
def accum(txt):
  return "-".join((txt[x].upper() + txt[x].lower()*x) for x in range(len(txt)))

