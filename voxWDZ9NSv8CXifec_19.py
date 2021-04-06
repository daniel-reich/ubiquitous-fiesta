
def lemonade(bills):
  change = 0
  for i in bills:
    if i>5:
      if change >= i-5:
        change -= i-5
      else:
        return False
    change += 5
  return True

