
def deepest(lst):
  count=0
  maxi=0
  print(str(lst))
  for i in range(len(str(lst))):
    if(str(lst)[i]=='['):
      count+=1
      if(count>maxi):
        maxi=count
    if(str(lst)[i]==']'):
      count-=1
    print(count)
  return(maxi)

