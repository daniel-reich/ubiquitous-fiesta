
def pirates_killed(gold, tolerance):
  distribution = [max(gold) - x for x in gold]
  walk_the_plank = [[a, b] for a, b in zip(distribution, tolerance)]
  return len([x for x in walk_the_plank if x[0] > x[1]]) >= 1

