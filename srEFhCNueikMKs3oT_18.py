
def consecutive_sum(n):
  total = 0
  for i in range(n):
    total += i
    for j in range(i+1,n):
      if total > n:
        total = 0
        break
      if total == n:
        return True
      total += j
  return False

