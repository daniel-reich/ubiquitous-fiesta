
def gold_distribution(gold):
  a = b = 0
  while gold:
    a += gold.pop() if gold[-1] > gold[0] else gold.pop(0)
    b += gold.pop() if gold[-1] > gold[0] else gold.pop(0)
  return [a, b]

