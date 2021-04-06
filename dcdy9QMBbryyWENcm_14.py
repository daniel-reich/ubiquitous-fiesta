
def total_cups(n):
  if n < 6:
    return n
  elif n >= 6:
    total = n + (n // 6)
    return total

