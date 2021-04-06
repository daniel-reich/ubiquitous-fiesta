
def lemonade(bills):
  change = {5:0,10:0}
  for b in bills:
    if b == 5:
      change[5]+=1
    if b == 10:
      if change[5]:
        change[5]-=1
        change[10]+=1
      else:
        return False
    if b == 20:
      if change[5] and change[10]:
        change[5]-=1
        change[10]-=1
      elif change[5] > 2:
        change[5]-=3
      else: 
        return False
  return True

