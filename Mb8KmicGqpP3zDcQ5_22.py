
def josephus(n, k):
  v = [i+1 for i in range(n)]
  return solve(v, 0, k-1)
  
def solve(v, start, k):
  if len(v) == 1:
    return v[0]
  
  index = (start + k) % len(v)
  v.pop(index)
​
  return solve(v, index, k)

