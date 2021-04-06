
def pile_of_cubes(m):
  i=1
  s=0
  while s<m:
    s+=i**3
    i+=1
  return i-1 if s==m else None

