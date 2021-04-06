
def num_ways(n, s):
  if s == {1}:
    return 1
  res = [0] * (n + 2)
  res[0] = 1
  res[1] = 1
  for i in range(2, n + 1) : 
    res[i] = sum(res[i-k] for k in s)
  return res[n]

