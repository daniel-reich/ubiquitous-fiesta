
def lemonade(bills):
  change = 0
  for bill in bills:
    print( bill, change)
    if bill == 10 or bill == 20:
      change -= bill - 5
    if change < 0:
      return False
    change += 5
  return True

