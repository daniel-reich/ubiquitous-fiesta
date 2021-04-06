
def add_odd_to_n(n):
  if n == 1: return 1
  sum = 0
  for i in range(1,n+1,2):
    sum = sum + i
  return sum

