
def last_dig(a, b, c):
  a = str(a)
  b = str(b)
  c = str(c)
  d = str(int(a[len(a)-1]) * int(b[len(b)-1])) 
  if int(d[len(d)-1]) == int(c[len(c)-1]):
    return True
  return False

