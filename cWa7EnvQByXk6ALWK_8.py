
def golden_ratio():
  a,b = 1,10
  for i in range(400):
    a,b = b,a+b
  st = str((b*10**100)//a)
  return "1." + st[1:-1]

