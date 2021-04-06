
def dolla_dolla_bills(money):
  return "{}${:,.2f}".format('-' if money < 0 else '', abs(money))

