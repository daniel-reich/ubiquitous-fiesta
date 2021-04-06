
def longest_run(lst):
  count=1
  newlist=[]
  lst.sort()
  for i in range(len(lst)-1):
    if lst[i]==lst[i+1]-1:
      count+=1
    elif lst[i]==lst[i+1]:
      pass
    else:
      newlist.append(count)
      count=1
  newlist.append(count)
  return(max(newlist))

