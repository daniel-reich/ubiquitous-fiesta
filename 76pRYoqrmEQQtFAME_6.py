
def is_astonishing(num):
  ns = str(num)
  for i in range(1,len(ns)):
    x = int(ns[:i]) if ns else 0
    y = int(ns[i:]) if ns else 0
    type = "AB"
    if x>y:
      type = "BA"
      x,y=y,x
    if num == (x+y)*(y-x+1)//2:
      return type + "-Astonishing"
  return False

