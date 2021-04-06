
def josephus(n):
  if n == 0:
    return False
  if n == 1:
    return 0
  A=[]
  for i in range(n):
    A.append(i)
  skip = 1
  idx = skip
  while len(A) > 1:
    A.pop(idx)
    idx = (idx + skip) % len(A)
  return A[0]

