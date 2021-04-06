
def pile_of_cubes(m):
  tot, n = 1, 1
​
  while tot <= m:
    if tot == m:
      return n
​
    n += 1
    tot += n ** 3

