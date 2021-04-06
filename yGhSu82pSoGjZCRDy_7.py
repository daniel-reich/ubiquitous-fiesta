
def seesaw(num):
  ns = str(num)
  if len(ns)==1 or num==None: return "balanced"
  l = len(ns) // 2
  if len(ns) % 2 == 1:
    ns = ns[:l] + ns[l+1:]
  nl, nr = int(ns[:l]), int(ns[l:])
  if nl > nr: return "left"
  elif nl < nr: return "right"
  else: return "balanced"

