
from fractions import gcd
def sim_prop_frac(max_den):
  s = set()
  for i in range(1,max_den+1):
    for j in range(1,i):
      val = gcd(i,j)
      if val==1:
        s.add(str(i)+'.'+str(j))
      else:
        i1 = i
        j1 = j
        while i1%val==0 and j1%val==0:
          i1//=val
          j1//=val
        s.add(str(i1)+'.'+str(j1))
  
  return len(list(s))

