
def shuffle_count(num):
  A=list(range(num))
  B=[A[0]]+[j for i in zip(A[len(A)//2:-1],A[1:len(A)//2]) for j in i]+[A[-1]]
  c=1
  while B!=A:
    B=[B[0]]+[j for i in zip(B[len(B)//2:-1],B[1:len(B)//2]) for j in i]+[B[-1]]
    c+=1
  return c

