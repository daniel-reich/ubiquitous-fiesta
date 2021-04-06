
def sum_of_holes(N):
  return sum(sum("469088".count(j) for j in str(i)) for i in range(1,N+1))

