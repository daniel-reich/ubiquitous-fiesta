
def lets_meet(d, va, vb):
  x = d/(va+vb)
  a = round(x//1)
  b = round(((x*60)%60)//1)
  c = round((((x*3600)%3600)%60)//1)
  return str(a)+"h "+str(b)+"min "+str(c)+"s"

