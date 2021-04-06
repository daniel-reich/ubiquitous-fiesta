
def ways_to_climb(n):
  ways = [1,1]
  for i in range(2,n+1):
    ways.append(sum(ways[i-2:i]))
  return ways[n]

