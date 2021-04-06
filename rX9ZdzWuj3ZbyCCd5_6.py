
def multiply_by_11(s):
  # recursive code here
  A=[int(x) for x in s[::-1]]+[0]
  B=[0]+[int(x) for x in s[::-1]]
  C=[]
  c=0
  for i in range(len(A)):
    if c+A[i]+B[i]>=10:
      C.append(str(c+A[i]+B[i]-10))
      c=1
    else:
      C.append(str(c+A[i]+B[i]))
      c=0
  if c==1:
    C.append(str(c))
  return ''.join(C[::-1])

