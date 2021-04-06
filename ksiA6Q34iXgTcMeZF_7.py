
def bonus(days):
  total = 0
  if days > 48:
    total = (8*325) + (8*550) + (days-48) * 600
  elif days > 40:
    total = (8*325) + (days-40) * 550
  elif days > 32:
    total = (days-32) * 325
  return total

