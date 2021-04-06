
def gold_distribution(gold):
  earn, i = [0, 0], 0
  while gold:
    earn[i] += gold.pop(0 if gold[0] >= gold[-1] else -1)
    i = (i + 1) % 2
  return earn

