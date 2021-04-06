
def add_bill(money):
  money = money.split(',')
  total = 0
  for element in money:
    if element[0] == 'd':
      total += int(element[1:-1]) * 1000 if element[-1] == 'k' else int(element[1:])
  return total

