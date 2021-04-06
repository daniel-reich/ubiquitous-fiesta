
def shuffle_count(num):
  A=list(range(1, num+1))
  B=[A[0]]+[y for x in zip(A[num//2:-1], A[1:num//2]) for y in x]+[A[-1]]
  c=1
  while B!=A:
    B=[B[0]]+[y for x in zip(B[num//2:-1], B[1:num//2]) for y in x]+[B[-1]]
    c+=1
  return c

