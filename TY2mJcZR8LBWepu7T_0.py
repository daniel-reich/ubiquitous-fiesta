
def risiko(attacker, defender):
  attacker.sort(reverse=True)
  defender.sort(reverse=True)
  return sum(a > d for a, d in zip(attacker, defender))

