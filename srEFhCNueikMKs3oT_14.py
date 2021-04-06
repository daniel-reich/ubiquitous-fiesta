
def consecutive_sum(n):
  for i in range(1,n-1):
    j = i + 1
    total = i
    while total < n:
      total = total + j 
      j += 1
      if total == n:
        return True 
  return False

