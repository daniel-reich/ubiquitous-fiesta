
def dolla_dolla_bills(money):
  if int(money) == money: m = str(money) + '.00'
  else: m = str(round(money, 2))
  return '-' + dolla_dolla_bills(-money) if money < 0 else '$' + ''.join(x + ',' if not len(m[i+1:-3]) % 3 else x for i, x in enumerate(m[:m.index('.')]))[:-1] + m[m.index('.'):]

