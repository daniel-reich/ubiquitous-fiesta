
def lets_meet(d, va, vb):
  t = d/(va+vb); s = (t-int(t))*3600
  return "%dh %dmin %ds"%(t,s//60,s%60)

