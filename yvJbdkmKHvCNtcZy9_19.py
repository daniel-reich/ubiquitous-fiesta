
def is_disarium(n):
  m=str(n)
  x=0
  for i in m:
    x += int(i)**int(m.index(i)+1)
  if x == n:
    return True
  else:
    return False

