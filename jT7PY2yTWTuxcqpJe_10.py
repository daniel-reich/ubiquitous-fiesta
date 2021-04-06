
def spiral_order(m):
  spr=[]
  while m:
    spr+=m.pop(0)
    m = list(zip(*m))[::-1]
  return spr

