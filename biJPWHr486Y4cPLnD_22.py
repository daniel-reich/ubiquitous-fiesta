
def chunkify(lst, size):
  arr=[]
  temp=[]
  c=0
  for i in lst:
    if c%size==0 and c!=0:
      arr.append(temp)
      temp=[]
    temp.append(i)
    c+=1
  arr.append(temp)
  return arr

