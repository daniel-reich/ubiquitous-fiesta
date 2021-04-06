
def final(rw, cl, ij):
  def r(row):
    m[row] = [x+1 for x in m[row]]
    return m
  
  def c(col):
    for i in range(len(m)):
      m[i][col] += 1
    return m
  
  m = [[0]*cl for i in range(rw)]
  for x in ij:
    eval(x[1])(int(x[0]))
    
  return m

