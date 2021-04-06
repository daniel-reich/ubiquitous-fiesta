
def straight_digital(n):
  d = ['Not Straight','Trivial Straight']
  n = str(n)
  if '-' in n: return d[0]  
  k = int(n[1])-int(n[0])
  if len(n)<3 or not all(int(n[i])-int(n[i-1])==k for i in range(1,len(n))):
      return d[0]
  if len(set(n))==1: return d[1]
  return k

