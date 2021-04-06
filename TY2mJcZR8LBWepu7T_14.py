
def risiko(attacker, defender):
  return sum([1 for x in zip(sorted(attacker,reverse=1),sorted(defender,reverse=1)) if x[0]>x[1]])

