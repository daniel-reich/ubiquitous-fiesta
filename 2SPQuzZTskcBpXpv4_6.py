
def euclidean(a, b):
  if a>=b:
    r=a%b
    if r==0:
      return b
    else:
      return euclidean(b,r)
  else:
    return euclidean(b,a)

