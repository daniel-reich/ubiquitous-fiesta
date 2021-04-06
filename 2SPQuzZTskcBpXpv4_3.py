
def euclidean(a, b):
  if a<b:
    a,b=b,a
  if a%b==0:
    return b
  else:
    return euclidean(b,a%b)

