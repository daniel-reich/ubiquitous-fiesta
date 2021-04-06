
def risiko(attacker, defender):
​
  armieslost = 0
​
  asorted = sorted(attacker)
  dsorted = sorted(defender)
  
  atv = len(attacker)
  dev = len(defender)
  
  print(asorted)
  print(dsorted)
  print("------------")
  print(dev)
  print(atv)
​
  if atv > dev:
    mlength = dev
  if atv < dev:
    mlength = atv
  if atv == dev:
    mlength = atv
​
  print(mlength)
​
  for x in range(0,mlength):
  
    if asorted[atv-1] > dsorted[dev-1]:
      armieslost += 1
    atv -= 1
    dev -= 1
  
  print("Armieslost is")
  print(armieslost)
  print("-------------------------")  
  return armieslost

