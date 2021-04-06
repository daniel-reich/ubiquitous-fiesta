
def sum_of_holes(N):
  return sum('046889'.count(k) for i in range(1,N+1) for k in str(i))

