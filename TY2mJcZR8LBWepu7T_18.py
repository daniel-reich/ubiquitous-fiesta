
def risiko(attacker, defender):
  dice = 0
  for a,b in zip(sorted(attacker)[::-1],sorted(defender)[::-1]):
    if a>b:
      dice+=1
  return dice

