
def dolla_dolla_bills(money):
  return '-' * (money<0) + '${:,.2f}'.format(abs(money))

