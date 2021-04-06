
def pile_of_cubes(m):
  n = 1
  while m>0:
    m-=n**3
    n+=1
  return n-1 if m==0 else None

