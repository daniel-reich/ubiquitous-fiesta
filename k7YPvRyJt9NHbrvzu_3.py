
def football(s):
  ans = {i:0 for i in range(s+1)}
  ans[0] = 1
  
  for i in [2,3,6,7,8]:
    for a in sorted(ans.keys())[::-1]:
      ans[a] = sum(ans[a-r*i] for r in range(0,1+s//i) if a-r*i>=0)
  
  return ans[s]

