
def champions(t):
  a=[[t[i]['name'],t[i]['wins']*3+t[i]['draws'],t[i]['scored']-t[i]['conceded']] for i in range(3)]
  b=[a[i][1] for i in range(3)]
  c=[a[i][2] for i in range(3)]
  d=[]
  e=[]
​
  for i in range(len(a)):
    if a[i][1]==max(b):
      d.append(a[i])
  if len(d)==1:
    return d[0][0]
​
  c=[d[i][2] for i in range(2)]
​
  if len(d)>1:
    print(d)
    for i in range(len(d)):
      if d[i][2]==max(c):
        e.append(d[i])  
    return e[0][0]

