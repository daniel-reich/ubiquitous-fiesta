
def risiko(attacker, defender):
  attacker = reversed(sorted(attacker))
  defender = reversed(sorted(defender))
  return sum(a > d for a, d in zip(attacker, defender))

