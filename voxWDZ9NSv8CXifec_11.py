
def lemonade(bills):
  cash = []
  for x in bills:
    if x == 5:
      cash.append(x)
    elif x == 10:
      if cash.count(5) >= 1:
        pass
      else : return False
    elif x == 20:
      if cash.count(5) >= 3:
        cash.remove(5)
        cash.remove(5)
        cash.remove(5)
      else : return False
  return True

