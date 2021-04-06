
def how_many_missing(lst):
  if len(lst)==0:
    return 0
  else:
    lst1=[]
    for i in range(min(lst),max(lst)+1):
      if i not in lst:
        lst1.append(i)
    return len(lst1)

