
def transpose_matrix(lst):
  x = lst
  if len(x) != 0:
    dim = (len(x[0]),len(x))
  else:
    dim = (0,0)
​
  out = []
​
  for i in range(0,dim[0]):
    out.append([])
​
  for i in range(0,len(x)):
    for k,v in enumerate(x[i]):
      out[k].append(v)
      
  return out

