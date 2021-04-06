
def change(x,t):
  l=x[:]
  for i in range(len(l)):
    j=1
    while j<=t:
      if i>=j and i<len(l)-j:l[i]-=1
      j+=1
  return l
x=[3,3,3,3,3,3,3]

