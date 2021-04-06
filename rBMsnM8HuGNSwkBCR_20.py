
def add_bill(money):
  return sum([int(el[1:-1]) * 1000 if el[0] == 'd' and el[-1] == 'k' else int(el[1:]) if el[0] == 'd' else 0 for el in money.split(',')])

