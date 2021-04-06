
def consecutive_sum(n):
  if n < 3: return False
  if n%2: return True
  for i in range(1, n//2 + 1):
    s, j = i, i + 1
    while s < n:
      s += j
      if s == n:
        return True
      j += 1
  return False

