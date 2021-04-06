
def pirates_killed(gold, tolerance):
  gold = [max(gold) - i for i in gold]
  print(tolerance, gold)
  diff = [x1 - x2 for (x1, x2) in zip(tolerance, gold)]
  print(diff)
  if min(diff) < 0:
    return True
  return False

