
def is_disarium(n):
  A=[int(x) for x in str(n)]
  return sum(A[i]**(i+1) for i in range(len(A)))==n

