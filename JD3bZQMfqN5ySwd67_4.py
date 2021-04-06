
from itertools import permutations
def is_vampire(n):
  if n<100:
    return "Normal Number"
  lst=[]
  if len(str(n))%2==0:
    lst=[int(''.join (i)) for i in list(permutations(str(n),len(str(n))//2))]
  else:
    for i in range (len(str(n))):
      lst=[]
      if i==len(str(n))-1:
        if (len(str(n))<=3):
          s1=str(n)[i:]
          s2=[str(n)[j] for j in range(len(str(n))) if j not in [i,i+1]]
        else:
          s1=str(n)[i]+str(n)[0]
          s2=[str(n)[j] for j in range(len(str(n))) if j not in [i,0]]
      else:
        s1=str(n)[i:i+len(str(n))//2]
        s2=[str(n)[j] for j in range(len(str(n))) if not j in range(i,i+len(str(n))//2)]
      s1=[s for s in s1]
      s1=(list(int(''.join(el)) for el in list(permutations(s1))))
      s2=(list(int(''.join(el)) for el in list(permutations(s2))))
      lst.append(s1)
      lst.append(s2)
      if sum([1 for i in range (len(lst[0])) for j in range (len(lst[1])) if lst[0][i]*lst[1][j]==n])>0:
        return "Pseudovampire"
    return 'Normal Number'
  cond= n in [lst[i]*lst[j] for i in range (len(lst)) for j in range (i+1,len(lst)) if lst[i]*lst[j]==n]
  return 'True Vampire' if cond and len(str(n))%2==0 else 'Normal Number'

