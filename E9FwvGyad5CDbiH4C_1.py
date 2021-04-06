
def block(lst):
  count=0
  for x in range(len(lst)):
    for i in range(len(lst[x])):
      if(lst[x][i]==2):
        count+=len(lst)-x-1   
  return(count)

