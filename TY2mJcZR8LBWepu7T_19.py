
def risiko(attacker, defender):
  defeat = 0
  n = min([len(attacker),len(defender)])
  sorted(attacker,reverse = True)
  sorted(defender,reverse = True)
  
  for i in range(n):
    if defender < attacker:
      defeat+=1
  return defeat

