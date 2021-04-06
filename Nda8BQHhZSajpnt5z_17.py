
def GCD(lst):
  li=[]
  for i in lst:
    lis=[]
    for j in range(1,i+1):
      if i%j==0:
        lis.append(j)
      else:
        continue
    li.append(lis)
  sets=[set(x) for x in li[1:]]
  return max(list(set(li[0]).intersection(*sets)))

