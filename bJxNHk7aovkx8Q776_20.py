
def gold_distribution(gold):
  res = [0, 0]
  turn = 0
  while gold:
    bigger = 0 if gold[0] >= gold[-1] else -1
    res[turn] += gold.pop(bigger)
    turn = not turn
  return res

