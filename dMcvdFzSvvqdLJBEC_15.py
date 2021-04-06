
def num_of_days(cost, savings, start):
  moneys = amount_money(start)
  total = 0
  day = 0
  enough = False
  while not enough:
    start_week = next(moneys)
    for a in range(7):
      total += start_week + a
      day += 1
      if cost - savings <= total:
        enough = True
        break
  return day
  
def amount_money(start):
  num = start
  while True:
    yield num
    num += 1

