
def binary_clock(time):
  h=[0 for i in range(2)]
  m=[0 for i in range(2)]
  s=[0 for i in range(2)]
  hh,mm,ss=time.split(":")
  h[0],h[1]=bin(int(hh[0]))[2:].zfill(4),bin(int(hh[1]))[2:].zfill(4)
  m[0],m[1]=bin(int(mm[0]))[2:].zfill(4),bin(int(mm[1]))[2:].zfill(4)
  s[0],s[1]=bin(int(ss[0]))[2:].zfill(4),bin(int(ss[1]))[2:].zfill(4)
  t=[]
  t.append([h[0]])
  t.append([h[1]])
  t.append([m[0]])
  t.append([m[1]])
  t.append([s[0]])
  t.append([s[1]])
  r=[]
  for i in range(4):
    a=""
    for j in range(len(t)):
      a+=t[j][0][i]
    r.append(list(a))
  r[0][0]=' '
  r[0][2]=' '
  r[0][4]=' '
  r[1][0]=' '
  for i in range(len(r)):
    r[i]=''.join(r[i])
  return r

