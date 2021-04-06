
def longest_time(*t):
  v = iter([1, 60, 3600])
  return max(t, key=lambda x: x/next(v))

