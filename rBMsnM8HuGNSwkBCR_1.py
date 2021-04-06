
def add_bill(money):
  return sum(int(i[1:]) for i in money.replace('k', '000').split(',') if i.startswith('d'))

