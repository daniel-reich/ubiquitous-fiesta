
def simple_numbers(a, b):
  A=[]
  for x in range(a,b+1):
    B=[int(y) for y in str(x)]
    if sum(B[i]**(i+1) for i in range(len(B)))==x:
      A.append(x)
  return A

