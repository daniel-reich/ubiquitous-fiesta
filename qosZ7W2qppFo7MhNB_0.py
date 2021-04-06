
def hex_distance(G):
  E = enumerate
  [x, y], [u, v] = [[x, y] for y, R in E(G) for x, c in E(R) if 'x' == c in R]
  for _ in range(v - y): x += x < u or -1
  return v + abs(x - u) / 2 - y

