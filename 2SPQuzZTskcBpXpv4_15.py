
def euclidean(a, b):
  if b > a:
    (a, b) = (b, a)
  if a % b == 0:
    return b
  return euclidean(b, a%b)

