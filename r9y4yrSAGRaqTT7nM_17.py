
def find_missing(lst):
  result=[]
  try:
    if(lst==None):
      return False
  except:
    pass
  try:
    if(len(lst)==0):
      return False
  except:
    pass
  for x in lst:
    if(len(x)==0):
      return False
    result.append(len(x))
  result=sorted(result)
  count=min(result)
  for x in result:
    if(count==x):
      count+=1
    else:
      return count

