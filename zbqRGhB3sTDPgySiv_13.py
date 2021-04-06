
def mod(base, key):
  if key < 2: return 0
  n = min(base, key)
  ans = 1
  fact = 1
  for i in range(1, n):
    fact *= i
    ans += fact
  return ans

