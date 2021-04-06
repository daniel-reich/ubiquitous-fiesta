
def pirates_killed(gold, tolerance):
  dist = [max(gold) - i for i in gold]
  return any([j < i for i, j in zip(dist, tolerance)])

