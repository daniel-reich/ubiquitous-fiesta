
def chunk(array, size):
  ans=[]
  a=[]
  for i in array:
    a.append(i)
    if len(a)==size:
      ans.append(a)
      a=[]
  if a: ans.append(a)
  return ans

