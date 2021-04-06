
def happy(n):
  l = []
  while True:
    s = sum((int(x))**2 for x in str(n))
    if s==4: return False
    if s==1: return True
    l.append(s)
    n=l[-1]

