
def lemonade(bills):
  money = [0,0]
  for b in bills:
    if b == 5:
      money[0] += 1
    elif b == 10:
      money[1] += 1
      if money[0]:
        money[0] -= 1
      else:
        return False
    elif b == 20:
      if money[1] and money[0]:
        money[1] -= 1
        money[0] -= 1
      elif money[0] >= 3:
        money[0] -= 3
      else:
        return False
  return True

