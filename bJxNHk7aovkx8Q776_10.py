
def gold_distribution(gold):
  totals, p = [0, 0], 0
  while gold:
    idx = -1 if gold[-1] > gold[0] else 0
    totals[p] += gold.pop(idx)
    p = 1 - p
  return totals

