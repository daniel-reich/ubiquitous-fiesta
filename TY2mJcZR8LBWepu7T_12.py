
def risiko(attacker, defender):
  DEF_loses = 0
  sort_ATK = sorted(attacker, reverse = True)
  sort_DEF = sorted(defender, reverse = True)
  
  for i in range(len(sort_ATK)):
    for j in range(len(sort_DEF)):
      if i == j:
        if sort_ATK[i] > sort_DEF[j]:
          DEF_loses += 1
  
  return DEF_loses

