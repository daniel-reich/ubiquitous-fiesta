
def triangle(p,a):
  res = []
  for i in range(1,p//2+1):
    for j in range(i,p//2+1):
      try:
        if a == round((p/2*(p/2-i)*(p/2-j)*(p/2-(p-i-j)))**0.5,5):
          if sorted([i,j,p-i-j]) not in res:
            res.append(sorted([i,j,p-i-j]))
      except:
        continue
  return res

