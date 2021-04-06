
def pirates_killed(gold, tolerance):
  x = max(gold)
  for i in range(0, len(gold)):
    gold[i] = x - gold[i]
    if gold[i] > tolerance[i]:
      return True
  return False

