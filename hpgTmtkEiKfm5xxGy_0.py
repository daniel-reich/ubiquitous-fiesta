
def paths(x, y):
  ans = 1
  for i in range(x):
    ans = ans*(x+y-i)//(i+1)
  return ans

