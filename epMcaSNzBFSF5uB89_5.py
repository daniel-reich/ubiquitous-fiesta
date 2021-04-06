
def currently_winning(scores):
  y,o,yc,oc,r=[],[],[],[],[]
  for i in range(len(scores)):
    if i%2==0:
      y.append(scores[i])     
    else:
      o.append(scores[i])
  #print(y,o)
  s,t=0,0
  for x,p in zip(y,o):
    s=s+x
    t=t+p
    yc.append(s)
    oc.append(t)
  #print(y,o,yc,oc)
  for j in range(len(yc)):
    #print(yc[j],oc[j])
    if int(yc[j]) > int(oc[j]):
      r.append('Y')
    elif int(yc[j]) == int(oc[j]):
      r.append('T')
    else:
      r.append('O')
  return r

