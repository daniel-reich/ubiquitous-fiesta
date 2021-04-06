
def euclidean(a, b):
  if(a<b):
    temp = a
    a = b
    b=temp
  r = a%b
  if(r==0):
    return b
  return euclidean(b,r)

