
def euclidean(a, b):
  [a,b] =sorted([a,b])
  while a%b:
    r=a%b
    a,b=b,r
  return b

