
def smallest(digits, value):
  total = 0
  while len(str(total)) != digits:
    total += value
  return total

