
def num_ways(n, s):
​
  depth = max(s) + 1
  ways = [1] + [0] * (depth-1)
​
  for step in range(1, n+1):
    way = sum(ways[(step-jump)%depth] for jump in s)
    ways[step%depth] = way
​
  return way

