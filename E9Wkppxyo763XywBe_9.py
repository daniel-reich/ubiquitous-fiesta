
def binary_clock(time):
  h1=time[0]
  h2=time[1]
  m1=time[3]
  m2=time[4]
  s1=time[6]
  s2=time[7]
  list=[]
  list.extend([h1,h2,m1,m2,s1,s2])
  ints=[int(x) for x in list]
  bins=[]
  for i in range(len(ints)):
    a=ints[i]
    if a==0:
      b=[0,0,0,0]
    if a==1:
      b=[0,0,0,1]
    if a==2:
      b=[0,0,1,0]
    if a==3:
      b=[0,0,1,1]
    if a==4:
      b=[0,1,0,0]
    if a==5:
      b=[0,1,0,1]
    if a==6:
      b=[0,1,1,0]
    if a==7:
      b=[0,1,1,1]
    if a==8:
      b=[1,0,0,0]
    if a==9:
      b=[1,0,0,1]
    bins.append(b)
  fix=[]
  for i in range(len(bins)):
    a=bins[i][0]
    fix.append(a)
  for i in range(len(bins)):
    a=bins[i][1]
    fix.append(a)
  for i in range(len(bins)):
    a=bins[i][2]
    fix.append(a)
  for i in range(len(bins)):
    a=bins[i][3]
    fix.append(a)
  b=fix[0:6]
  c=fix[6:12]
  d=fix[12:18]
  e=fix[18:24]
  b2=[str(x) for x in b]
  c2=[str(x) for x in c]
  d2=[str(x) for x in d]
  e2=[str(x) for x in e]
  b2[0]=' '
  b2[2]=' '
  b2[4]=' '
  c2[0]=' '
  j=""
  b3=j.join(b2)
  c3=j.join(c2)
  d3=j.join(d2)
  e3=j.join(e2)
  last=[]
  last.extend([b3,c3,d3,e3])
  return last

