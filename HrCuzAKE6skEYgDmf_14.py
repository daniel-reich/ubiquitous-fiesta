
def pairs(l):
  a=[]
  if len(l)%2: #odd
    for i in range(len(l)//2 + 1):
      a.append([l[i], l[-1-i]])
  else:
    for i in range(len(l)//2):
      a.append([l[i], l[-1-i]])   
  return a

