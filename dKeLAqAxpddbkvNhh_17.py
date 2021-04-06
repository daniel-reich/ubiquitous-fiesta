
def group_seats(lst, n):
  A = lst
  N=n
  Z=[]
  for i in range(N):
    Z.append(0)
​
  out_N=0
  for m in range(len(A)):
    Am=A[m]
    B = []
    for j in range(len(Am)-N+1):
      B = Am[j:j+N]
      if B==Z:
        out_N = out_N+1
  return out_N

