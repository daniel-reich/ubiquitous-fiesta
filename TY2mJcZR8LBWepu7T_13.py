
def risiko(attacker, defender):
  attacker.sort(reverse = True) 
  defender.sort(reverse = True)
  return sum(list(map(lambda x,y: x > y, attacker, defender)))

