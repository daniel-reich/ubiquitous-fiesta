
def rolls(lst):
  lastRoll = lst[0]
  total = lst[0]
  for i, roll in enumerate(lst[1:]):
    lastRoll = lst[i]
    if lastRoll == 1:
      total += 0
    elif lastRoll == 6:
      total += roll *2
    else:
      total += roll
  return total

