
def pascal_row(n):
  ans = [1]*(n+1)
  for i in range(n):
    ans[i+1] = ans[i]*(n-i)//(i+1)
  return ans

