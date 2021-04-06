
def scale_tip(l):
  a = sum(l[:l.index("I")])
  b = sum(l[l.index("I") + 1 ::])
  if a > b:
    return "left"
  elif a < b:
    return "right"
  else:
    return "balanced"

