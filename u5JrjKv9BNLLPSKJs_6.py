
def num_ways(n, s):
  ans = [1]
  if n == 0:
    return 1
  for i in range(1,n+1):
    total = 0
    for t in s:
      if i-t >= 0:
        total += ans[i-t]
    ans.append(total)
  return ans[n]

