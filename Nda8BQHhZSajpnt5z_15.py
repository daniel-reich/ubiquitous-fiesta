
def GCD(lst):
  newdict={}
  for i in range(1, max(lst)):
      for n in lst:
        if n%i==0:
          if i in newdict:
           newdict[i]+=1
          else:
            newdict[i]=1
  newList=[i for i in newdict if newdict[i]==len(lst)]
  return max(newList)

