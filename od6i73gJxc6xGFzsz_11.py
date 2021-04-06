
def is_slidey(n):
  n = list(map(int, list(str(n))))
  is_differ_by_one = [True if abs(x - y) == 1 else False for x, y in zip(n[:-1], n[1:])]
  return all(is_differ_by_one)

