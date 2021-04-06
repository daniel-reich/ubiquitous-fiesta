
import re
def unravel(txt):
  a,fork=(txt),[]
  b= re.sub('\[',',',a)
  b=re.sub('\]',',',b)
  lst = [c for c in b.split(',') if c !='']
  for i in range (len(lst)):
    if len(lst[i].split('|'))==1:
      if len(fork) ==0:
        fork.append(lst[i])
      else:
        for j in range (len(fork)):
          fork[j]+=lst[i]
    else:
      if (i==0):
        for j in range (len(lst[i].split('|'))):
          fork.append(lst[i].split('|')[j])
      else:
        comb=lst[i].split('|')
        fork =[''.join((x,y)) for x in fork for y in comb]
  return sorted(fork)

