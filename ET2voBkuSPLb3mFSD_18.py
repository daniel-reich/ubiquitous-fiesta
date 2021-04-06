
def sum_every_nth(numbers, n):
  if len(numbers) < n:
    return 0
    
  s = 0
  for i in range(n-1,len(numbers), n):
    s+= numbers[i]
  return s

