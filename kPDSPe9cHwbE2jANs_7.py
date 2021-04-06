
def cards_needed(n):
  if n < 0: return "invalid"
  if n == 0: return 0
  return 3 * n - 1 + cards_needed(n-1)

