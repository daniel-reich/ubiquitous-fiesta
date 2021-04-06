
def risiko(attacker, defender):
  attacker = sorted(attacker, reverse=True)
  defender = sorted(defender, reverse=True)
  return sum(a>d for a,d in zip(attacker, defender))

