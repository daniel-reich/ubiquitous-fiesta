
def risiko(attacker, defender):
  a = sorted(attacker)[::-1]
  b = sorted(defender)[::-1]
  lost = 0
  if len(a) < len(b):
    for i in range(0, len(a)):
      if a[i] > b[i]:
        lost += 1
  else : 
    for i in range(0, len(b)):
      if a[i] > b[i]:
        lost += 1
  return lost

