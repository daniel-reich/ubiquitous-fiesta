
def pirates_killed(gold, tolerance):
  
  maxgold = max(gold)
  print(maxgold)
  for i in range(len(gold)):
    dif = maxgold - gold[i]
    if dif>tolerance[i]:
      return True
  
  return False

