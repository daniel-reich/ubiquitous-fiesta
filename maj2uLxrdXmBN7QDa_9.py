
def bishop(start, end, n):
  a1,a2 = trans(start)
  b1,b2 = trans(end)
  if (a1+a2+b1+b2)%2:
    return False
  if n==0:
    return (a1,a2) == (b1,b2)
  if n==1:
    return abs(a1-b1) == abs(a2-b2)
  return True
​
def trans(coor):
  return ('abcdefghijk'.index(coor[0]),'12345678'.index(coor[1]))

