
def pirates_killed(gold, tolerance):
  gs = [max(gold) - x for x in gold]
  return any([x < y for x, y in zip(tolerance, gs)])

