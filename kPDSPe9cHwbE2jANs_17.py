
def cards_needed(n):
  if n < 0:
    return 'invalid'
  else:
    return int(n * (3 * n + 1)/2)

