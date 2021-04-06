
def euclidean(a, b):
  if a<b:
    return euclidean(b,a)
  
  r=a%b
  if r==0:
    return b
  else:
    return euclidean(b,r)

