
def bonus(days):
  x = 325
  y = 550 
  z = 600 
  if days <= 32:
    return 0
  elif days <= 40:
    return (days -32) * x
  elif days <= 48:
    return ((days -40) * y) + 8*x
  else:
    return ((days- 48) * z) + 8*x + 8*y

