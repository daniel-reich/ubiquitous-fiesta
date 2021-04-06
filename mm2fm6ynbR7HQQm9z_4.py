
def knights_jump(s):
  a = 'ABCDEFGH'
  n = '12345678'
  x,y = a.index(s[0]),n.index(s[1])
  ret = []
  if x>1:
    if y>0: ret.append(a[x-2]+n[y-1])
    if y<7: ret.append(a[x-2]+n[y+1])
  if x<6:
    if y>0: ret.append(a[x+2]+n[y-1])
    if y<7: ret.append(a[x+2]+n[y+1])
  if y>1:
    if x>0: ret.append(a[x-1]+n[y-2])
    if x<7: ret.append(a[x+1]+n[y-2])
  if y<6:
    if x>0: ret.append(a[x-1]+n[y+2])
    if x<7: ret.append(a[x+1]+n[y+2])
  return ','.join(sorted(ret,key=lambda i:i[1]))

