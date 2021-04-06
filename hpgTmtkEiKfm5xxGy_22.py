
def paths(x, y, memo={}):
  key = frozenset((x, y))
  if key in memo: return memo[key]
  if x == 0 or y == 0: return 1
  memo[key] = paths(x - 1, y, memo) + paths(x, y - 1, memo)
  return memo[key]

