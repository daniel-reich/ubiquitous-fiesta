
def freed_prisoners(prison):
  if prison[0] == 0: 
    return 0
  s, inv = 0, 0
  for p in prison:
    p = (p, not p)[inv]
    if p:
      s += 1
      inv = not inv
  return s

