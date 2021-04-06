
def euclidean(a, b):
  if b==0: return a
  return euclidean(b, a%b)

