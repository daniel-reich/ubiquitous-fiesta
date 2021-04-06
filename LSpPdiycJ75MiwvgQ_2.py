
def grid_pos(lst):
  m,n = lst
  return comb(m+n,n)
​
def comb(n,k):
  ans = 1
  for i in range(k):
    ans = ans*(n-i)//(i+1)
  return ans

