
def simplify(txt):
  d=txt.split("/")
  b,c=int(d[0]), int(d[1])
  for i in range(b, 0, -1):
    if b%i==0 and c%i==0 and c/i==1:
      return str(int(b/c))
    elif b%i==0 and c%i==0:
      return str(int(b/i)) + "/" + str(int(c/i))
  return txt

