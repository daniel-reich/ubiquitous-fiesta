
import itertools
directions = ((1,0), (0, 1), (-1, 0), (0, -1))
def add(p1, p2):
  return (p1[0] + p2[0], p1[1] + p2[1])
  
def inbounds(pos, size):
  return 0 <= pos[0] < size and 0 <= pos[1] < size
  
def spiral(n):
  iter_d = itertools.cycle(directions)
  c = ((n-1)//2, (n-1)//2)
  yield c
  dist = 1
  while True:
    for _ in range(2):
      d = next(iter_d)
      for __ in range(dist):
        c = add(c, d)
        if not inbounds(c, n):
          return
        yield c
    dist += 1
      
def spiral_matrix(side, string):
  m = [[None, ] * side for _ in range(side)]
  chars = itertools.chain(iter(string), itertools.repeat('+'))
  positions = spiral(side)
  for p in positions:
    m[p[1]][p[0]] = next(chars)
  return m

