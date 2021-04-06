
def num_ways(n, s):
  if len(s) == 1 and list(s)[0] == 1:
    return 1
  res = [0 for i in range(n+1)]
  res[0], res[1] = 1, 1
  for i in range(2, n+1):
    for step in s:
      if i - step < 0: continue
      res[i] = res[i] + res[i - step] 
  return res[n]

