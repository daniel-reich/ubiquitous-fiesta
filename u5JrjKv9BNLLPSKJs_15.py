
def num_ways(n, s):
  ways = {-i:0 for i in range(1,len(s))}
  ways[0]=1
  for k in range(1,n+1):
    ways[k] = sum(ways[k-i] for i in s)
  return ways[n]

