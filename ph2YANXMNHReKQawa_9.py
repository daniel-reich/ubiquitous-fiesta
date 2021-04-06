
def length_element(r,i):
  new=[]
  count=-1
  first=len(r)
  second=0
  for j in r:
    new.append(j)
  for item in new:
    count+=1
    if count==i:
      second=item
  newer=[]
  newer.append(first)
  newer.append(second)
  return newer

