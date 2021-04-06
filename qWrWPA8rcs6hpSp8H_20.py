
def determinant(m):
  if any([(lambda x: (not isinstance(x,list)))(x) for x in m]):
    return 'Error: not a 2-dim list'
  if any([(lambda x,y: (not isinstance(m[x][y],int)) and (not isinstance(m[x][y],float)))(x,y) for x in range(len(m)) for y in range(len(m[x]))]):
    return 'Error: invalid list element'
  if any([(lambda x: len(x)!=len(m[0]))(x) for x in m]):
    return 'Error: list elements have different length'
  if len(m)!=len(m[0]):
    return 'Error: not a square matrix'
​
  if len(m)==1:
    return m[0][0]
  ret=0
  for i in range(len(m[0])):
    subm=[[x[y] for y in range(len(m[0])) if y!=i] for x in m[1:]]
    ret+=(1 if i%2==0 else -1)*m[0][i]*determinant(subm)
#    print(subm)
  return ret

