
def accum(txt):
  return "-".join((ch*(idx+1)).capitalize() for idx,ch in enumerate(txt))

