
def num_ways(n, s):
  ways = [1]
  for x in range(n):
    c = 0
    for y in list(s):
      if x+1>=y:
        c+=ways[-y]
    ways.append(c)
  return ways[-1]

