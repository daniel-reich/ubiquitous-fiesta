
def chunkify(lst, size):
  s1=[]
  for i in range(0,len(lst),size):
    s1.append(lst[i:i+size])
  return s1

