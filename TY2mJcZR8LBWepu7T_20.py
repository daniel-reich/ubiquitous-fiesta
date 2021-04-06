
def risiko(attacker, defender):
  mi =  min(len(attacker), len(defender))
  attacker = sorted(attacker, reverse=True)
  defender = sorted(defender, reverse=True)
  x = 0
  for i in range(0, mi):
    if attacker[i] > defender[i]:
      x+=1
  return x

