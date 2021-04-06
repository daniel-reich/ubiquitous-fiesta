
def bonus(days):
  if days>48:
    return 600*(days-48)+7000
  if days>40:
    return 500*(days-40)+2600
  if days>32:
    return 325*(days-32)
  return 0

