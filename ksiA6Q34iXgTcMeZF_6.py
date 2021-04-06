
def bonus(days):
  if days <= 32:
    return 0
  if days <= 40:
    return (days - 32) * 325
  if days <= 48:
    return (days - 40) * 550 + 8 * 325
  return (days - 48) * 600 +  8 * 550 + 8 * 325

