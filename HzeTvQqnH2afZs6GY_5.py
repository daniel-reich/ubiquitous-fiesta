
def generate_rug(n, direction):
  A=list(range(n))
  M=[[]]*n
  if direction=="left":
    for i in range(n):
      M[i]=(A[1:i+1][::-1]+A[:n-i])
  else:
    for i in range(n):
      M[i]=(A[:n-i][::-1]+A[1:i+1])
  return M

