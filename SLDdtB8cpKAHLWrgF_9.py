
from itertools import permutations
def greater_permutation(expr, nums):
  lst=list(permutations(nums))
  for j in range (len(lst)):
    i,out=0,''
    for c in expr:
      if c in 'abc':
        out+=str(lst[j][i])
        i+=1
      else:
        out+=c
    if j==0:
      maxx=eval(out)
      s=out + ' = '
    if (eval(out)>=maxx):
      if(eval(out) == int(eval(out))):
        maxx=int(eval(out))
      else:
        maxx=round(eval(out),2)
      s=out + ' = '
  return s + str(maxx)

