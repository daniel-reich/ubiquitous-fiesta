
def bonus(days):
  if days < 33:
    return 0
  elif days < 41:
    return (days - 32) * 325
  elif days < 49:
    return (days - 40) * 550 + 325 * 8
  else:
    return (days - 48) * 600 + (550 + 325) * 8

