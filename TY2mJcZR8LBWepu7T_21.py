
def risiko(attacker, defender):
  return sum(x>y for x,y in zip(sorted(attacker,reverse=True),sorted(defender,reverse=True)))

