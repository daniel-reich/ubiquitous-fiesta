
from itertools import permutations
def next_number(num):
 numst=str(num)
 if len(numst)==1:return int(numst)
 for l in range(2,len(numst)+1):
  perms=sorted(["".join(i) for i in permutations(numst[-l:])])
  if numst[-l:]!=perms[-1]:
   if l==len(numst):
       perms = sorted(list(set(perms)))
       return int(perms[perms.index(numst) + 1])
   elif l>2:
       return int(numst[0:-l]+perms[perms.index(numst[-l:]) + 1])
   return int(numst[0:-l]+perms[-1])
 return int(numst)

