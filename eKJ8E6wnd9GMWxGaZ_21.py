
def dolla_dolla_bills(money):
  if money < 0:
    return '-' + "${:,.2f}".format(abs(money))
  
  return "${:,.2f}".format(money)

