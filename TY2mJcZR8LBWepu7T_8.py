
def risiko(attacker, defender):
  return sum([1 for a,d in zip(sorted(attacker, reverse=True), sorted(defender, reverse=True)) if a > d])

