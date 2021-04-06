
def add_bill(money):
  total = 0
  for bill in money.split(','):
    if bill.startswith('d'):
      if bill.endswith('k'):
        total += 1000 * int(bill[1:-1])
      else:
        total += int(bill[1:])
  return total

