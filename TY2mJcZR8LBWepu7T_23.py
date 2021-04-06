
def risiko(attacker, defender):
  count = 0 
  attacker.sort()
  defender.sort()
  for i,j in zip(attacker[::-1],defender[::-1]):
    if i > j:
      count += 1
​
​
  return count

