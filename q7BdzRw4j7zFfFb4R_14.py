
def merge_arrays(a, b):
  lst = []
  c=[]
  if len(a)>len(b):
    c = a[len(b):]
  else:
    c = b[len(a):]
  for i,j in zip(a,b):
    lst.append(i)
    lst.append(j)
  for k in c:
    lst.append(k)
  return lst

