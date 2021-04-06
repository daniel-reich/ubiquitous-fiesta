
def total_cups(n):
  free_cups = n // 6
  if n >= 6:
    return n + free_cups
  else:
    return n

