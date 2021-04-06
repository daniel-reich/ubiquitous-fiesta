
def pascals_triangle(row):
  p = [0,1,0]
  for _ in range(row):
    p = [0] + [sum(z) for z in zip(p,p[1:])] + [0]
  return ' '.join(map(str,p[1:-1]))

