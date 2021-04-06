
def spider_vs_fly(s, f):
  d='ABCDEFGH'
  si, fi=d.index(s[0]), d.index(f[0])
  sn, fn=int(s[1]), int(f[1])
  k=min(abs(si-fi), 8-abs(si-fi))
  path=[]
  if k>2:
    for i in range(sn, 0,-1):
      path.append('{}{}'.format(s[0],i))
    path.append('A0')
    for i in range(1, fn+1):
      path.append('{}{}'.format(f[0],i))
  elif 0<k<3:
    if k==abs(si-fi):
      if si>fi and sn>=fn:
        for i in range(sn,fn-1,-1):
          path.append('{}{}'.format(s[0],i))
        for i in range(si-1,fi-1,-1):
          path.append('{}{}'.format(d[i],fn))
      elif si>fi and sn<=fn:
        for i in range(si,fi-1,-1):
          path.append('{}{}'.format(d[i],sn))
        for i in range(sn+1,fn+1):
          path.append('{}{}'.format(f[0],i))
      elif si<fi and sn>=fn:
        for i in range(sn,fn-1,-1):
          path.append('{}{}'.format(s[0],i))
        for i in range(si+1,fi+1):
          path.append('{}{}'.format(d[i],fn))
      elif si<fi and sn<=fn:
        for i in range(si,fi-1,-1):
          path.append('{}{}'.format(d[i],sn))
        for i in range(sn-1,fn-1,-1):
          path.append('{}{}'.format(s[0],i))
          
  return '-'.join(path)

