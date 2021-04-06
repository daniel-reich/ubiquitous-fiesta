
def split(txt):
  open = 0
  clusters = []
  cluster = ''
  for c in txt:
    cluster += c
    if c == '(':
      open += 1
    if c == ')':
      open -= 1
    if open == 0:
      clusters.append(cluster)
      cluster = ''
  return clusters

