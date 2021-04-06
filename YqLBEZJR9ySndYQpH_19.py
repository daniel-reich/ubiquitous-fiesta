
def staircase(n):
  out = ""
  r = abs(n)
  if n<0:
    r = abs(n)+1
  for x in range(r):
    t = ""
    r_y = abs(n)- (x+1)
    r_h = x+1
    if n<0:
      r_y = abs(n) - x
      r_h = x
    for y in range(r_y):
      t+="_"
    for y in range(r_h):
      t+="#"
    t+="\n"
    out+=t
  if n<0:
    out = reverse(out)
  return out[:-1]
​
​
def reverse(out):
  t=[]
  e=""
  for x in out:
    if x!="\n":
      e+=x
    else:
      e+="\n"
      t.append(e)
      e=""
  e=""
  for x in range(len(t)-1):
    e+=t[(len(t)-1)-x]
  return e

