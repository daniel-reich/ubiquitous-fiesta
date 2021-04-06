
def risiko(attacker, defender):
  
  attacker = list(reversed(sorted(attacker)))
  defender = list(reversed(sorted(defender)))
  
  lost_defenders = 0
  length = len(attacker)
  
  if len(attacker) != len(defender):
    l = [len(attacker), len(defender)]
    length = min(l)
    del l
  
  for n in range(0, length):
    
    a = attacker[n]
    d = defender[n]
    
    if a > d:
      lost_defenders += 1
  
  return lost_defenders

