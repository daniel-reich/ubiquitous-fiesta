
def pirates_killed(gold, tolerance):
  diff = [max(gold)-coin for coin in gold]
  alive = [a - b for a, b in zip(diff, tolerance)]
  aboveZero = [i for i in alive if i > 0]
  return len(aboveZero) > 0

