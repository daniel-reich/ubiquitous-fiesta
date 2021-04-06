
def risiko(attacker, defender):
  return sum(1 for a,b in zip(sorted(attacker,reverse=True),sorted(defender,reverse=True)) if b < a)

