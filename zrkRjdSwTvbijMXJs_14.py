
def ssum(x,y):
    s=''
    for i in range(len(x)):
        s+=str((int(x[i])+int(y[i]))%10)
    return s
​
def ssub(x,y):
    t=''
    for i in range(len(x)):
        t+=str((int(x[i])-int(y[i])+10)%10)
    return t
  
def encrypt(plncode, pad):
  p=pad[:len(plncode)+5]
  A=[plncode[i:i+5] for i in range(0,len(plncode),5)]
  B=[p[i:i+5] for i in range(0,len(pad),5)]
  C=B[1:]
  D=[B[0]]+[ssub(x,y) for x, y in zip(A,C)]
  return ''.join(D)
​
def decrypt(cypcode, pad):
  p=pad[:len(cypcode)]
  A=[cypcode[i:i+5] for i in range(0,len(cypcode),5)]
  B=[p[i:i+5] for i in range(0,len(pad),5)]
  if A[0]!=B[0]:
    return "Error: Key IDs don't match."
  else:
    C=A[1:]
    D=B[1:]
    E=[ssum(x,y) for x, y in zip(C,D)]
    return ''.join(E)

