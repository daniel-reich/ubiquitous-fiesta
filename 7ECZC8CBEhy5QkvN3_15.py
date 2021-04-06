
def how_many_walls(n, w, h):
  sum_ = 0
  count = 0
  wallSquare = w * h
  while sum_ <= n:
    sum_ += wallSquare
    count += 1
  return count - 1

