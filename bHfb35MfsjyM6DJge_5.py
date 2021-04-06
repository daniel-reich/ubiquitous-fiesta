
def route_diff(directions):
  def move(n, a):
    if n == 'N':
      return [a[0], a[1] + 1]
    elif n == 'S':
      return [a[0], a[1] - 1]
    elif n == 'E':
      return [a[0] + 1, a[1]]
    else:
      return [a[0] - 1, a[1]]
  m = [0, 0]
  for i in directions:
    m = move(i, m)
  return len(directions) - abs(m[0]) - abs(m[1])

