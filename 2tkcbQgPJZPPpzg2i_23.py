
def sum_of_holes(N):
  h=0
  for i in range(1,N+1):
    for j in str(i):
      if j in ["0","4","6","9"]:
        h+=1
      elif j=="8":
        h+=2
  return h

