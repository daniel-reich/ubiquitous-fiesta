
def add_bill(money):
  money = [x for x in money.split(',') if x[0] == 'd']
  return sum(int(x[1:-1])*1000 if x[-1] == 'k' else int(x[1:]) for x in money)

