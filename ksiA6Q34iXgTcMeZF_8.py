
def bonus(days):
  if days <= 32:
    return 0
  elif days <= 40:
    return (days - 33 + 1) * 325
  elif days <= 48:
    return (40 - 33 + 1) * 325 + (days - 41 + 1) * 550
  else:
    return ((40 - 33 + 1) * 325 + (48 - 41 + 1) * 550 + 
    (days - 49 + 1) * 600)

