
def cards_needed(n):
  if n < 0 :
    return 'invalid'
  sum = 0
  for i in range(1,n+1):
    sum = sum + 2 + 3*(i-1)
  return sum

