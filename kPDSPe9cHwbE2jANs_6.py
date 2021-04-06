
def cards_needed(n):
  if n < 0:
    return 'invalid'
  res = 0
  for x in range(1, n+1):
    res += x * 2 + (x * 2 - 2) / 2
  return res

