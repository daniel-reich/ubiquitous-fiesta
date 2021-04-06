
def sum_of_holes(N):
  count_holes = lambda n: [1,0,0,0,1,0,1,0,2,1][int(n)]
  return sum(count_holes(j) for i in range(1,N+1) for j in str(i))

