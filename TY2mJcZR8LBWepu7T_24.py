
def risiko(attacker, defender):
  attacker = sorted(attacker, reverse=True)
  defender = sorted(defender, reverse=True)
  return sum(1 for a, d in zip(attacker, defender) if a > d)

