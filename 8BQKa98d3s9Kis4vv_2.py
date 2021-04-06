
def final(r,c,i):
  m=[c*[0]for _ in range(r)]
  for x in i:
    k=int(x[0])
    if'r'==x[1]:
      for y in range(c):m[k][y]+=1
    else:
      for y in range(r):m[y][k]+=1
  return m

