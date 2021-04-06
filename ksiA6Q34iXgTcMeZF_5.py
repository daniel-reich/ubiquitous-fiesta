
def bonus(days):
  return sum(0 if i < 32 else 325 if i < 40 else 550 if i < 48 else 600 for i in range(days))

