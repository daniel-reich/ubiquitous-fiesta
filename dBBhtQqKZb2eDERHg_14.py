
def numberSequence(n):
  if n<1: return "-1"
​
  m=(n+1)//2
​
  t =[str(x) for x in range(m,0,-1)]
  tt=[str(x) for x in range(1,m+1)]
  
​
  if len(t+tt)>n: return ' '.join(t+tt[1:])
  
  return ' '.join(t+tt)

