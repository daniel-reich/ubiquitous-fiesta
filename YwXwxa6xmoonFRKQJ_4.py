
def josephus(n):
  if n < 1:
    return False
  
  circle = list(range(n))
  i = 0
  while len(circle) > 1:
    i = (i + 1) % len(circle)
    circle.pop(i)
  assert len(circle)
  return circle[0]

