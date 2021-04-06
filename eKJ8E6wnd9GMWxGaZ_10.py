
import locale
def dolla_dolla_bills(money):
  return ('$'if money >=0 else '-$')+'{:,.2f}'.format(abs(money))

