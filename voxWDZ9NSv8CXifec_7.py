
def lemonade(bills):
  change = 0
  for i in bills:
    change -= i-5
    if change<0:
      return False
    change+=5
  return True

