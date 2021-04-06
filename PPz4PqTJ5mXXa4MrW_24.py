
um=[1,2]
​
def ulam(n):
  global um
  while len(um)<n:
    for i in range(um[-1]+1,um[-1]*2):
      c=0
      for j in range(len(um)):
        if i-um[j] in um and um[j]*2!=i:c+=1
        if c>2:break
      if c==2:
        um+=[i]
        break
  return um[n-1]

